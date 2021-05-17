from collections import Counter

from anthony.tables import db
import sqlite3

LEN_WEIGHT = 1
CHAR_WEIGHT = 1
INXED_WEIGHT = 3


def length_difference(s1, s2):
    l1, l2 = len(s1), len(s2)
    return 0.0 if l1 > 2 * l2 else (l1 if l1 <= l2 else (l2 - (l1 - l2))) / l2


def character_difference(s1, s2):
    l2, char_count1, char_count2 = len(s2), Counter(s1), Counter(s2)
    return 1 - sum([abs(char_count1[c] - char_count2[c]) for c in char_count2]) / l2


def index_difference(s1, s2):
    l1 = len(s1)
    return sum([1 if (i < l1 and s1[i] == c) else 0 for i, c in enumerate(s2)]) / len(
        s2
    )


def comparator(s1, s2):
    """Compares two strings (s1, s2)
    Returns dict of measures of similiarity
    Each measure answers the question:
        With regard to X (measure) how similiar is s1 to s2.
    """
    return {
        "length": length_difference(s1, s2),
        "characters": character_difference(s1, s2),
        "index": index_difference(s1, s2),
    }


def distance(
    s1,
    s2,
):
    return (
        (length_difference(s1, s2) * LEN_WEIGHT)
        + (character_difference(s1, s2) * CHAR_WEIGHT)
        + (index_difference(s1, s2) * INXED_WEIGHT)
    ) / (LEN_WEIGHT + CHAR_WEIGHT + INXED_WEIGHT)


db.c.create_function("_distance", 2, distance, deterministic=True)
sqlite3.enable_callback_tracebacks(True)


def suggest(word, limit=5):
    result = db.execute(
        f""" SELECT Word
             FROM word
             WHERE length (word) > 1
             ORDER BY _distance(?, word) DESC
             LIMIT {limit}
         """,
        (word,),
    )
    return result

