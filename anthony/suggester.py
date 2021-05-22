from anthony.models import db
from anthony.utility.distance import compare

from dsorm import Comparison

db.c.create_function("_distance", 2, compare, deterministic=True)


def suggest(word, limit=5, affinity=[]):
    affinity_sql = ("AND " + Comparison.is_in("DocumentId", affinity).sql()) if affinity else ""
    result = db.execute(
        f""" SELECT DISTINCT Word
             FROM word
             JOIN document_words ON word.id = document_words.WordId
                                {affinity_sql}
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
