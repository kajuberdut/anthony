from pathlib import Path

from anthony.document import index, search
from anthony.tables import db, word_index, word_table
from anthony.utility.string_functions import sentencize


def init_db():
    db.initialize()
    db.execute(word_index)


if __name__ == "__main__":
    from datetime import datetime

    init_db()

    with open(Path.cwd() / "sample.txt", encoding="utf-8") as fh:
        pp = list(enumerate(sentencize(fh.read())))

    start = datetime.now()
    index([{"text": t, "data": t, "__id__": i} for i, t in pp])
    print(f"Parse and Insert Time: {datetime.now() - start}")

    start = datetime.now()
    result = search("bride hampshire random military")
    print(f"Search Time: {datetime.now() - start}")

    words = {
        word["id"]: word["Word"]
        for word in word_table.select(column=["id", "Word"]).execute()
    }

    for r in result:
        print(r)

    # TODO: fuzzy matching
