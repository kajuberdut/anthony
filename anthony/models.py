from enum import Enum

from dsorm import Column, Database, Pragma, RawSQL, Table, make_table

DB_PATH = "anythony.db"

db = Database(DB_PATH, is_default=True)

conf = Pragma.from_dict(
    {
        "foreign_keys": 1,  # Foreign key enforcement is off by default in SQLite
        "temp_store": 2,  # This database is considered "expendible"
    }
)


@make_table
class WordType(Enum):
    STEM = 1
    BRANCH = 2
    STOP = 3


word_table = Table(
    table_name="word",
    column=[
        Column.id(),
        Column(column_name="Word", nullable=False, unique=True),
        Column(
            column_name="WordType",
            python_type=WordType,
            nullable=False,
        ),
    ],
)

word_index = RawSQL("CREATE INDEX IF NOT EXISTS word_word_idx ON word(Word)")

word_stem_table = Table(
    table_name="word_stem",
    column=[
        Column.id(),
        Column(
            column_name="BranchWordId", python_type=int, nullable=False, unique=True
        ),
        Column(column_name="StemWordId", python_type=int, nullable=False),
    ],
    constraints=[
        word_table.fkey("BranchWordId"),
        word_table.fkey("StemWordId"),
    ],
)

synonym_table = Table(
    table_name="synonym",
    column=[
        Column.id(),
        Column(column_name="FromWordId", python_type=int, nullable=False),
        Column(column_name="ToWordId", python_type=int, nullable=False),
    ],
    constraints=[
        RawSQL("UNIQUE(FromWordId, ToWordId)"),
        word_table.fkey("FromWordId"),
        word_table.fkey("ToWordId"),
    ],
)

document_table = Table(
    table_name="document",
    column=[
        Column.id(),
        Column(column_name="DocumentType"),
        Column(column_name="DocIdent"),
        Column(column_name="Data"),
        Column(column_name="DataType"),
    ],
    constraints=[RawSQL("UNIQUE(DocumentType, DocIdent)")],
)

document_words = Table(
    table_name="document_words",
    column=[
        Column.id(),
        Column(column_name="DocumentId", python_type=int, nullable=False),
        Column(column_name="WordId", python_type=int, nullable=False),
        Column(column_name="StemWordId", python_type=int, nullable=False),
        Column(column_name="WordIndex", python_type=int)
    ],
    constraints=[
        word_table.fkey("WordId"),
        word_table.fkey("StemWordId"),
        RawSQL("UNIQUE(DocumentId, WordId, WordIndex)"),
        RawSQL(
            """CONSTRAINT fk_Document_Word
    FOREIGN KEY (DocumentId)
    REFERENCES document(id)
    ON DELETE CASCADE"""
        ),
    ],
)


def init_db():
    db.initialize()
    db.execute(word_index)
