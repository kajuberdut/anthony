from time import perf_counter_ns

LEN_WEIGHT = 1
INDEX_WEIGHT = 3
CONTAINS_WEIGHT = 1


def length_compare(s1, s2):
    """Returns a number between 0 and 1:
        How similiar len(s1) is to len(s2).
    If s1 is more than 2X the length of s2 similiarity is 0.
    If s1 is shorter than s2, similiarity is the ratio of len(s1) to len(s2).
    If s1 is longer than s2, but less than double:
        similiarity is the ratio of the amount len(s1) exceeds len(s2) to len(s2).
    Strings of identical length will have a length similiarity of 1.
    """
    l1, l2 = len(s1), len(s2)
    return 0.0 if l1 > 2 * l2 else (l1 if l1 <= l2 else (l2 - (l1 - l2))) / l2


def index_compare(s1, s2):
    """Returns a number between 0 and 1:
        What percentage of the char x at index n of s2:
            are identical to char x of index n of s1
        If the character is not identical:
            half a point is given for next neighbor characters
    If s1 starts with s2, they will have an index similiarity of 1.
    """
    l1 = len(s1)
    return sum(
        [
            0
            if i > l1
            else 1
            if (i < l1 and s1[i] == c)
            else (
                0.5
                if ((i + 1 < l1 and s1[i + 1]) == c or (i > 0 and s1[i - 1] == c))
                else 0
            )
            for i, c in enumerate(s2)
        ]
    ) / len(s2)


def compare(
    s1,
    s2,
):
    if not s1 or not s2:
        return 0
    s1, s2 = s1.lower(), s2.lower()
    return (
        (length_compare(s1, s2) * LEN_WEIGHT)
        + (index_compare(s1, s2) * INDEX_WEIGHT)
        + (1 if s1 in s2 else 0) * CONTAINS_WEIGHT
    ) / (LEN_WEIGHT + INDEX_WEIGHT + CONTAINS_WEIGHT)


def compare_info(s1, s2):
    """Compares two strings (s1, s2)
    Returns dict of comparison measures.
    Each measure answers the question:
        With regard to X (measure) how similiar is s1 to s2.
    """
    result = {
        "weights": {
            "length weight": LEN_WEIGHT,
            "index weight": INDEX_WEIGHT,
            "contains weight": CONTAINS_WEIGHT,
            "total weight": LEN_WEIGHT + INDEX_WEIGHT + CONTAINS_WEIGHT,
        },
        "scores": {},
        "times": {},
    }
    start = perf_counter_ns()
    result["scores"]["length"] = length_compare(s1, s2)
    result["times"]["length time ns"] = str(perf_counter_ns() - start)
    start = perf_counter_ns()
    result["scores"]["index"] = index_compare(s1, s2)
    result["times"]["index time ns"] = str(perf_counter_ns() - start)
    start = perf_counter_ns()
    result["scores"]["contains"] = 1 if s1 in s2 else 0
    result["times"]["contains time ns"] = str(perf_counter_ns() - start)
    result["scores"]["total score"] = (
        (result["scores"]["length"] * LEN_WEIGHT)
        + (result["scores"]["index"] * INDEX_WEIGHT)
        + (result["scores"]["contains"] * CONTAINS_WEIGHT)
    )
    result["scores"]["compare rating"] = (
        result["scores"]["total score"] / result["weights"]["total weight"]
    )
    return result

# python -m nuitka --module distance.py
