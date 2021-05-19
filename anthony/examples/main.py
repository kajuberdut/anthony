from pathlib import Path
from time import perf_counter_ns

from anthony.document import index, search
from anthony.models import init_db
from anthony.suggester import suggest
from anthony.utility.string_functions import sentencize

init_db()

# Open the text of Pride and Prejudice
# https://www.gutenberg.org/files/1342/1342-0.txt
with open(Path.cwd() / "sample.txt", encoding="utf-8") as fh:
    pp = list(enumerate(sentencize(fh.read())))

# Index the set of sentences
start = perf_counter_ns()
index([{"text": t, "data": t, "__id__": i} for i, t in pp])
print(
    f"Parsed and inserted {len(pp)} sentences in: {(perf_counter_ns() - start)/1e+9} Seconds\n\n"
)

# Search for some text
search_text = "abominable"
start = perf_counter_ns()
result = search(search_text, limit=5)
print(f"Search for text '{search_text}': {(perf_counter_ns() - start)/1e+9} Seconds\n")
for r in enumerate(result):
    print(f"""Result: {r[0]}: "{r[1]["Data"]}" """ f"""\nHits: {r[1]["Hits"]}""")

# Suggest alternatives for a word
start = perf_counter_ns()
print(f"\n\nWord suggestions for 'booz': {[s['Word'] for s in suggest('bookz')]}")
print(f"Suggestion Time: {(perf_counter_ns() - start)/1e+9} Seconds")
