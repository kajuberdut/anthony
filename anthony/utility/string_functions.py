import re



TOKEN_END = re.compile(r"[^\da-z]")
SENTENCE_END = re.compile(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s")
GREEDY_WHITESPACE = re.compile(r"\s+")

STOP_WORDS = frozenset(
    """
    i me my myself we our ours ourselves you your yours yourself yourselves
    he him his himself she her hers herself it its itself they them their
    theirs themselves what which who whom this that these those am is are
    was were be been being have has had having do does did doing a an the
    and but if or because as until while of at by for with about against
    between into through during before after above below to from up down in
    out on off over under again further then once here there when where why
    how all any both each few more most other some such no nor not only own
    same so than too very s t can will just don should now
    """.split()
)

def sentencize(text):
    text = re.sub(GREEDY_WHITESPACE, " ", text)
    return [s.strip() for s in re.split(SENTENCE_END, text) if len(s) > 3]


def tokenize(text):
    return [
        w
        for w in re.split(TOKEN_END, text.lower())
        if w not in STOP_WORDS and len(w) > 1
    ]

