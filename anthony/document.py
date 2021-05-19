from hashlib import md5
from uuid import uuid4

from dsorm import Column, Comparison
from dsorm.dsorm import RawSQL

from anthony.models import Column, Table, WordType, db
from anthony.utility.stemmer import stem
from anthony.utility.string_functions import tokenize

db.c.create_function("_stem", 1, stem, deterministic=True)


def save_words(words):
    words = list(set(words))
    temp_name = f"temp_words_{str(uuid4())[-12:]}"
    temp_table = Table(
        table_name=temp_name,
        column=[
            Column(column_name="word", nullable=False, unique=True),
            RawSQL("stem TEXT AS (_stem(word)) STORED"),
        ],
        temp=True,
    )
    temp_table.execute()

    db.c.executemany(
        f"""INSERT INTO [{temp_name}](Word) 
            SELECT :newword
            WHERE NOT EXISTS (  SELECT 1 
                                FROM word 
                                WHERE word.Word = :newword
                             )""",
        ({"newword": w} for w in words),
    )

    db.c.executescript(
        f""" INSERT INTO word(Word, WordType)
             SELECT newwords.word, {WordType.BRANCH.value}
             FROM [{temp_name}] newwords
             WHERE newwords.word != newwords.stem;

             INSERT INTO word(Word, WordType)
             SELECT newwords.stem, {WordType.STEM.value}
             FROM [{temp_name}] newwords
             WHERE true
             ON CONFLICT (Word) DO NOTHING;

             INSERT INTO word_stem(BranchWordId, StemWordId)
             SELECT branch.id, stem.id
             FROM [{temp_name}] newwords
             JOIN word branch ON newwords.word != newwords.stem
                                AND newwords.word = branch.Word
                                AND branch.WordType = {WordType.BRANCH.value}
             JOIN word stem ON newwords.stem = stem.Word AND stem.WordType = {WordType.STEM.value};
         """
    )
    temp_table.drop().execute()


def index(documents):
    documents = [
        {
            **d,
            **{
                "__id__": d.get("__id__", md5(d["text"].encode("utf-8")).hexdigest()),
                "words": tokenize(d["text"]),
            },
        }
        for d in documents
    ]
    db.c.executemany(
        """INSERT INTO document(Data, DocumentType, DocIdent, DataType) values (?,?,?,?) ON CONFLICT DO NOTHING""",
        [
            (
                d.get("data"),
                d.get("document_type", "GENERIC"),
                d["__id__"],
                str(type(d["data"])),
            )
            for d in documents
        ],
    )

    save_words([words for d in documents for words in d["words"]])

    temp_name = f"temp_doc_words_{str(uuid4())[-12:]}"
    temp_table = Table(
        table_name=temp_name,
        column=[
            Column(column_name="DocIdent", nullable=False),
            Column(column_name="word", nullable=False),
        ],
        temp=True,
    )

    temp_table.execute()
    db.c.executemany(
        f"""INSERT INTO [{temp_name}](DocIdent, word) values (?,?) ON CONFLICT DO NOTHING""",
        [(d["__id__"], words) for d in documents for words in d["words"]],
    )

    db.c.execute(
        f""" INSERT INTO document_words(DocumentId, WordId, StemWordId)
    SELECT DISTINCT d.id, w.id, IFNULL(ws.StemWordId, w.id)
    FROM [{temp_name}] dw
    JOIN document d ON dw.DocIdent = d.DocIdent
    JOIN word w ON dw.word = w.word
    LEFT JOIN word_stem ws ON w.id = ws.BranchWordId
    WHERE true
    ON CONFLICT DO NOTHING;
    """
    )
    temp_table.drop().execute()


def search(text, limit=10):
    return db.execute(
        f"""WITH search_words AS (
	SELECT CASE 
				WHEN w.WordType = 1
					THEN w.Word
				ELSE
					w.Word || '|' || s.Word
			END WordPath
		 , IFNULL(ws.StemWordId, w.id) StemWordId
		 , w.id WordId
	FROM word w 
	LEFT JOIN word_stem ws ON w.id = ws.BranchWordId
	LEFT JOIN word s ON ws.StemWordId = s.id
	WHERE ({Comparison.is_in("w.Word", tokenize(text)).sql()})
)
SELECT d.DocIdent
	 , d.Data 
	 , COUNT(*) HitCount
	 , group_concat( DISTINCT CASE 
						WHEN WordPath = w.Word 
							THEN WordPath
						WHEN sw.WordId = dw.WordId
							THEN w.Word
						ELSE WordPath || '|' || w.Word 
					 END
					) Hits
FROM search_words sw
JOIN document_words dw ON sw.StemWordId = dw.StemWordId
JOIN document d ON dw.DocumentId = d.id
LEFT JOIN word w ON dw.WordId = w.id
GROUP BY d.DocIdent, d.Data
ORDER BY HitCount DESC
LIMIT {limit}"""
    )


# python -m nuitka --module document.py
