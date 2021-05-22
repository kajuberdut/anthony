from anthony.models import db
from anthony.utility.distance import compare

db.c.create_function("_distance", 2, compare, deterministic=True)


def suggest(word, limit=5):
    result = db.execute(
        f""" SELECT DISTINCT Word
             FROM word
             JOIN document_words ON word.id = document_words.WordId
             WHERE length (word) > 1
             ORDER BY _distance(?, word) DESC
             LIMIT {limit}
         """,
        (word,),
    )
    if len(result) > 0:
        return [r["Word"] for r in result]
    else:
        return None

# python -m nuitka --module suggester.py
