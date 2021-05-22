from pathlib import Path

from anthony import index, init_db, search
from anthony.utility.string_functions import highlight, sentencize

init_db()

# Open the text of Pride and Prejudice
# https://www.gutenberg.org/files/1342/1342-0.txt
with open(Path.cwd() / "sample.txt", encoding="utf-8") as fh:
    pp = sentencize(fh.read())

# Index the set of sentences
index([{"text": t, "data": t} for t in pp])


# Search for some text
s = search("probably despise abominable bingly", limit=1, suggestions=True)
print(f'Did You Mean: "{s["DidYouMean"]}"?')
hits, text = s["Results"][0]["Hits"], s["Results"][0]["Data"]
print(highlight(hits, text, left_tag="__", right_tag="__"))
