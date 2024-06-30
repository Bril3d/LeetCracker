<p align="center">
  <svg width="100px" height="100px" viewBox="0 0 24 24" role="img" xmlns="http://www.w3.org/2000/svg"><path d="M13.483 0a1.374 1.374 0 0 0-.961.438L7.116 6.226l-3.854 4.126a5.266 5.266 0 0 0-1.209 2.104 5.35 5.35 0 0 0-.125.513 5.527 5.527 0 0 0 .062 2.362 5.83 5.83 0 0 0 .349 1.017 5.938 5.938 0 0 0 1.271 1.818l4.277 4.193.039.038c2.248 2.165 5.852 2.133 8.063-.074l2.396-2.392c.54-.54.54-1.414.003-1.955a1.378 1.378 0 0 0-1.951-.003l-2.396 2.392a3.021 3.021 0 0 1-4.205.038l-.02-.019-4.276-4.193c-.652-.64-.972-1.469-.948-2.263a2.68 2.68 0 0 1 .066-.523 2.545 2.545 0 0 1 .619-1.164L9.13 8.114c1.058-1.134 3.204-1.27 4.43-.278l3.501 2.831c.593.48 1.461.387 1.94-.207a1.384 1.384 0 0 0-.207-1.943l-3.5-2.831c-.8-.647-1.766-1.045-2.774-1.202l2.015-2.158A1.384 1.384 0 0 0 13.483 0zm-2.866 12.815a1.38 1.38 0 0 0-1.38 1.382 1.38 1.38 0 0 0 1.38 1.382H20.79a1.38 1.38 0 0 0 1.38-1.382 1.38 1.38 0 0 0-1.38-1.382z"/></svg>
</p>
<p align="center">
    <h1 align="center"></h1>
</p>
<p align="center">
    <em> `Leetcode problems automation`</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/Bril3d/LeetCracker?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Bril3d/LeetCracker?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Bril3d/LeetCracker?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Bril3d/LeetCracker?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat&logo=tqdm&logoColor=black" alt="tqdm">
	<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=flat&logo=scikit-learn&logoColor=white" alt="scikitlearn">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">
	<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style=flat&logo=SciPy&logoColor=white" alt="SciPy">
	<img src="https://img.shields.io/badge/Selenium-43B02A.svg?style=flat&logo=Selenium&logoColor=white" alt="Selenium">
	<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
	<br>
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
</p>
<hr>

## 🔗 Quick Links

> - [📍 Overview](#-overview)
> - [📦 Features](#-features)
> - [📂 Repository Structure](#-repository-structure)
> - [🧩 Modules](#-modules)
> - [🚀 Getting Started](#-getting-started)
>   - [⚙️ Installation](#️-installation)
>   - [🤖 Running ](#-running-)
>   - [🧪 Tests](#-tests)
> - [🛠 Project Roadmap](#-project-roadmap)
> - [🤝 Contributing](#-contributing)
> - [📄 License](#-license)
> - [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

 `overview`
Leetcracker is a Python script that streamlines solving Leetcode problems by automating the entire process using Selenium. This tool is ideal for competitive programmers and coding enthusiasts looking to enhance their problem-solving efficiency.

With Leetcracker, you can automatically log in, solve, and scrape Leetcode questions effortlessly. The script can handle up to 200 problems in an hour, making it a powerful addition to your coding toolkit.
---

## 📦 Features

 `features`
1. ### Automated Problem-Solving
   Leetcracker can automatically solve Leetcode problems for you.

2. ### Seamless Login
   The script manages user authentication, ensuring a smooth login process.

3. ### Solution Scraping
   Leetcracker can scrape and organize your accepted solutions, helping you keep track of your progress and maintain a personal archive of your achievements.

4. ### Resume Solving from Where You Left Off
   The script remembers the last problem it solved, allowing it to resume solving from where you left off.
---

## 📂 Repository Structure

```sh
└── /
    ├── Auth.py
    ├── LICENSE
    ├── LeetcodeScraper.py
    ├── LeetcodeSolver.py
    ├── README.md
    ├── main.py
    ├── problems
    │   ├── best-time-to-buy-and-sell-stock.json
    │   ├── binary-number-with-alternating-bits.json
    │   ├── binary-search-tree-to-greater-sum-tree.json
    │   ├── binary-search.json
    │   ├── binary-tree-cameras.json
    │   ├── binary-tree-inorder-traversal.json
    │   ├── binary-tree-level-order-traversal-ii.json
    │   ├── binary-tree-level-order-traversal.json
    │   ├── binary-tree-maximum-path-sum.json
    │   ├── binary-tree-paths.json
    │   ├── binary-tree-postorder-traversal.json
    │   ├── binary-tree-preorder-traversal.json
    │   ├── binary-tree-pruning.json
    │   ├── binary-tree-right-side-view.json
    │   ├── binary-tree-tilt.json
    │   ├── binary-tree-zigzag-level-order-traversal.json
    │   ├── binary-trees-with-factors.json
    │   ├── binary-watch.json
    │   ├── bitwise-and-of-numbers-range.json
    │   ├── bitwise-xor-of-all-pairings.json
    │   ├── boats-to-save-people.json
    │   └── break-a-palindrome.json
    ├── requirements.txt
    └── utils
        └── utils.py
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                       | Summary                                        |
| ---                                                                                        | ---                                            |
| [LeetcodeScraper.py](https://github.com/Bril3d/LeetCracker/blob/master/LeetcodeScraper.py) |  `LeetcodeScraper.py` |
| [main.py](https://github.com/Bril3d/LeetCracker/blob/master/main.py)                       |  `main.py`            |
| [Auth.py](https://github.com/Bril3d/LeetCracker/blob/master/Auth.py)                       |  `Auth.py`            |
| [LeetcodeSolver.py](https://github.com/Bril3d/LeetCracker/blob/master/LeetcodeSolver.py)   |  `LeetcodeSolver.py`  |
| [requirements.txt](https://github.com/Bril3d/LeetCracker/blob/master/requirements.txt)     |  `requirements.txt`   |

</details>

<details closed><summary>problems</summary>

| File                                                                                                                                                      | Summary                                                                            |
| ---                                                                                                                                                       | ---                                                                                |
| [break-a-palindrome.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/break-a-palindrome.json)                                             |  `problems/break-a-palindrome.json`                       |
| [binary-tree-level-order-traversal.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-tree-level-order-traversal.json)               |  `problems/binary-tree-level-order-traversal.json`        |
| [binary-search-tree-to-greater-sum-tree.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-search-tree-to-greater-sum-tree.json)     |  `problems/binary-search-tree-to-greater-sum-tree.json`   |
| [binary-search.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-search.json)                                                       |  `problems/binary-search.json`                            |
| [binary-tree-paths.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-tree-paths.json)                                               |  `problems/binary-tree-paths.json`                        |
| [binary-tree-tilt.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-tree-tilt.json)                                                 |  `problems/binary-tree-tilt.json`                         |
| [binary-tree-zigzag-level-order-traversal.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-tree-zigzag-level-order-traversal.json) |  `problems/binary-tree-zigzag-level-order-traversal.json` |
| [binary-tree-preorder-traversal.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-tree-preorder-traversal.json)                     |  `problems/binary-tree-preorder-traversal.json`           |
| [bitwise-and-of-numbers-range.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/bitwise-and-of-numbers-range.json)                         |  `problems/bitwise-and-of-numbers-range.json`             |
| [binary-tree-cameras.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-tree-cameras.json)                                           |  `problems/binary-tree-cameras.json`                      |
| [bitwise-xor-of-all-pairings.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/bitwise-xor-of-all-pairings.json)                           |  `problems/bitwise-xor-of-all-pairings.json`              |
| [binary-trees-with-factors.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-trees-with-factors.json)                               |  `problems/binary-trees-with-factors.json`                |
| [binary-tree-inorder-traversal.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-tree-inorder-traversal.json)                       |  `problems/binary-tree-inorder-traversal.json`            |
| [binary-tree-right-side-view.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-tree-right-side-view.json)                           |  `problems/binary-tree-right-side-view.json`              |
| [best-time-to-buy-and-sell-stock.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/best-time-to-buy-and-sell-stock.json)                   |  `problems/best-time-to-buy-and-sell-stock.json`          |
| [binary-number-with-alternating-bits.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-number-with-alternating-bits.json)           |  `problems/binary-number-with-alternating-bits.json`      |
| [binary-watch.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-watch.json)                                                         |  `problems/binary-watch.json`                             |
| [binary-tree-postorder-traversal.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-tree-postorder-traversal.json)                   |  `problems/binary-tree-postorder-traversal.json`          |
| [binary-tree-level-order-traversal-ii.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-tree-level-order-traversal-ii.json)         |  `problems/binary-tree-level-order-traversal-ii.json`     |
| [binary-tree-pruning.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-tree-pruning.json)                                           |  `problems/binary-tree-pruning.json`                      |
| [binary-tree-maximum-path-sum.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/binary-tree-maximum-path-sum.json)                         |  `problems/binary-tree-maximum-path-sum.json`             |
| [boats-to-save-people.json](https://github.com/Bril3d/LeetCracker/blob/master/problems/boats-to-save-people.json)                                         |  `problems/boats-to-save-people.json`                     |

</details>

<details closed><summary>utils</summary>

| File                                                                         | Summary                                    |
| ---                                                                          | ---                                        |
| [utils.py](https://github.com/Bril3d/LeetCracker/blob/master/utils/utils.py) |  `utils/utils.py` |

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.12.3`

### ⚙️ Installation

1. Clone the  repository:

```sh
git clone https://github.com/Bril3d/LeetCracker/
```

2. Change to the project directory:

```sh
cd LeetCracker
```

3. Install the dependencies:

```sh
> pip install -r requirements.txt
```

### 🤖 Running 

Use the following command to run :

```sh
> python main.py
```

---

## 🛠 Project Roadmap

- [X] `► Still Working on it`


---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/Bril3d/LeetCracker/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Bril3d/LeetCracker/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/Bril3d/LeetCracker/issues)**: Submit bugs found or log feature requests for .

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/Bril3d/LeetCracker/
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License

This project is protected under the [MIT](https://github.com/Bril3d/LeetCracker/blob/main/LICENSE) License. For more details, refer to the [LICENSE](https://github.com/Bril3d/LeetCracker/blob/main/LICENSE) file.

---

## 👏 Acknowledgments

- Inspired by leetcoder *-*

  
[**Return**](#-quick-links)

---
