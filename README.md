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
* Document search
* Text suggestions


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
The following code snippets show basic usage. They assume a variable pp has been created and points to a sequence of sentences of the text of Pride and Prejudice.  
For full code, including the imports needed see [simple_example.py](https://github.com/kajuberdut/anthony/blob/main/anthony/examples/simple_example.py)

### Index
Indexing a document adds it to or updates it in the search store.
```python
index([{"text": t, "data": t} for t in pp])
```

### Search
```python
s = search("probably despise abominable bingly", limit=1, suggestions=True)
hits, text = s["Results"][0]["Hits"], s["Results"][0]["Data"]
print(highlight(hits, text, left_tag="__", right_tag="__"))
```  
#### Result:
> The vague and unsettled suspicions which uncertainty had produced of what Mr. Darcy might have been doing to forward her sister’s match, which she had feared to encourage as an exertion of goodness too great to be __probable__, and at the same time dreaded to be just, from the pain of obligation, were proved beyond their greatest extent to be true! He had followed them purposely to town, he had taken on himself all the trouble and mortification attendant on such a research; in which supplication had been necessary to a woman whom he must __abominate__ and __despise__, and where he was reduced to meet, frequently meet, reason with, persuade, and finally bribe, the man whom he always most wished to avoid, and whose very name it was punishment to him to pronounce.

Highlight is an easy way to wrap formatting around each of the searched word within the document. Here we wrap __ to get bold in markdown.

#### Suggestions
```python
print(f'Did You Mean: "{s["DidYouMean"]}"?')
```

    > Did You Mean: "probably despise abominable bingley"?  

Since we passed "suggestions=True" we get back this suggestion which corrects "bingly" to "bingley".  



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


<!-- CONTRIBUTING -->
## Contributing
See the [open issues](https://github.com/kajuberdut/anthony/issues) for a list of proposed features (and known issues).

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
