<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/kajuberdut/anthony">
    <img src="https://raw.githubusercontent.com/kajuberdut/anthony/main/images/Icon.svg" alt="Logo" width="160" height="160">
  </a>

  <h2 align="center">Anthony: Find it with Python</h2>

  <p align="center">
    Tony, Tony, look around, help me find what can’t be found
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a>
      <!-- <ul>
        <li><a href="#further-examples">Further Examples</a></li>
      </ul> -->
    </li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Anthony is a document search engine written in Python.


### Features
* Document indexing
* Search
* Word suggestion


<!-- GETTING STARTED -->
## Getting Started

<!-- To get a local copy up and running follow these simple steps. -->
<!-- ### Installing with pip -->
  <!-- ```sh
  pip install anthony
  ``` -->

For information about cloning and dev setup see: [Contributing](#Contributing)


<!-- USAGE EXAMPLES -->
## Usage
Here is an example showing basic usage.

```python
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
    pp = enumerate(sentencize(fh.read()))

# Index the set of sentences
start = perf_counter_ns()
index([{"text": t, "data": t, "__id__": i} for i, t in pp])
print(
    f"Parsed and inserted {len(list(pp))} sentences in: {(perf_counter_ns() - start)/1e+9} Seconds\n\n"
)

# Search for some text
search_text = "abominable"
start = perf_counter_ns()
result = search(search_text, limit=5)
print(f"Search for text '{search_text}': {(perf_counter_ns() - start)/1e+9} Seconds\n")
for r in enumerate(result):
    print(
        f"""Result: {r[0]}: "{r[1]["Data"]}" """
        f"""\n\tHits: {" ".join([f"{h[0]}({h[1]})" for h in zip(r[1]["Hits"].split(","), r[1]["HitIndexes"].split(","))])}"""
    )

# Suggest alternatives for a word
start = perf_counter_ns()
search_term = 'bingly'
print(f"\n\nWord suggestions for '{search_term}': {[s['Word'] for s in suggest(search_term, limit=3)]}")
print(f"Suggestion Time: {(perf_counter_ns() - start)/1e+9} Seconds")

```

```
Parsed and inserted 0 sentences in: 0.3 Seconds


Search for text 'abominable': 0.02 Seconds

Result: 0: "Oh! _that_ abominable Mr. Darcy! My father’s opinion of me does me the greatest honour, and I should be miserable to forfeit it." 
        Hits: abominable(5)
Result: 1: "Who would have thought that she could be so thin and small?” “She is abominably rude to keep Charlotte out of doors in all this wind." 
        Hits: abominable|abomin|abominably(17)
Result: 2: "But his pride, his abominable pride—his shameless avowal of what he had done with respect to Jane—his unpardonable assurance in acknowledging, though he could not justify it, and the unfeeling manner in which he had mentioned Mr. Wickham, his cruelty towards whom he had not attempted to deny, soon overcame the pity which the consideration of his attachment had for a moment excited." 
        Hits: abominable(5)
Result: 3: "It seems to me to show an abominable sort of conceited independence, a most country-town indifference to decorum.” “It shows an affection for her sister that is very pleasing,” said Bingley." 
        Hits: abominable(7)
Result: 4: "The vague and unsettled suspicions which uncertainty had produced of what Mr. Darcy might have been doing to forward her sister’s match, which she had feared to encourage as an exertion of goodness too great to be probable, and at the same time dreaded to be just, from the pain of obligation, were proved beyond their greatest extent to be true! He had followed them purposely to town, he had taken on himself all the trouble and mortification attendant on such a research; in which supplication had been necessary to a woman whom he must abominate and despise, and where he was reduced to meet, frequently meet, reason with, persuade, and finally bribe, the man whom he always most wished to avoid, and whose very name it was punishment to him to pronounce."
        Hits: abominable|abomin|abominate(104)


Word suggestions for 'bingly': ['bingley', 'single', 'kindly']
Suggestion Time: 0.06 Seconds
```

<!-- ### Further Examples
* [A Practical Example](https://github.com/kajuberdut/anthony/blob/main/examples/PracticalExample.py)
* [Compound WHERE clauses and Tables from Enum](https://github.com/kajuberdut/anthony/blob/main/examples/AdvancedWhere.py)
* [Joins and Database from Dict](https://github.com/kajuberdut/anthony/blob/main/examples/JoinExample.py)
* [Custom Type Handling & Column Defaults](https://github.com/kajuberdut/anthony/blob/main/examples/CustomTypeHandlerAndDefault.py)
* [Store Python Objects with Pickle Data Handler](https://github.com/kajuberdut/anthony/blob/main/examples/PickleData.py)
* [Configuration](https://github.com/kajuberdut/anthony/blob/main/examples/AdvancedConfiguration.py) -->


<!-- ROADMAP -->
<!-- ## Roadmap

Needed features:
* Subquery/CTE support
* Grouping/Aggregates
* Order/Limit/Offset -->

See the [open issues](https://github.com/kajuberdut/anthony/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
<!-- 3. Add tests, we aim for 100% test coverage [Using Coverage](https://coverage.readthedocs.io/en/coverage-5.3.1/#using-coverage-py) -->
4. execute: py.test --cov-report xml:cov.xml --cov
5. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the Branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

### Cloning / Development setup
1. Clone the repo and install
    ```sh
    git clone https://github.com/kajuberdut/anthony.git
    cd anthony
    pipenv install --dev
    ```
2. Run tests
    ```sh
    pipenv shell
    py.test
    ```
  For more about pipenv see: [Pipenv Github](https://github.com/pypa/pipenv)



<!-- LICENSE -->
## License

Distributed under the UnLicense. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Patrick Shechet - patrick.shechet@gmail.com

Project Link: [https://github.com/kajuberdut/anthony](https://github.com/kajuberdut/anthony)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kajuberdut/anthony.svg?style=for-the-badge
[contributors-url]: https://github.com/kajuberdut/anthony/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kajuberdut/anthony.svg?style=for-the-badge
[forks-url]: https://github.com/kajuberdut/anthony/network/members
[stars-shield]: https://img.shields.io/github/stars/kajuberdut/anthony.svg?style=for-the-badge
[stars-url]: https://github.com/kajuberdut/anthony/stargazers
[issues-shield]: https://img.shields.io/github/issues/kajuberdut/anthony.svg?style=for-the-badge
[issues-url]: https://github.com/kajuberdut/anthony/issues
[license-shield]: https://img.shields.io/badge/License-unlicense-orange.svg?style=for-the-badge
[license-url]: https://github.com/kajuberdut/anthony/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/patrick-shechet