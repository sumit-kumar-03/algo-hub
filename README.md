# algo-hub

Personal algorithms and data structures practice in Python. Every problem is a standalone script with its own test suite.

## Contents

| Folder | What's in it | Problems |
|---|---|---|
| [`fundamentals/`](fundamentals/) | Core algorithms: binary search, sorting, recursion, divide and conquer, graph traversal | 7 |
| [`elements_of_programming_interviews/`](elements_of_programming_interviews/) | *Elements of Programming Interviews in Python*, limited to the book's study plan, organized by chapter and section. C0/C1 sections include extra practice variants graded Easy to Hard. See its [README](elements_of_programming_interviews/README.md) for the plan and progress. | 372 + 12 design |

```
algo-hub/
├── fundamentals/
│   ├── 01_binary_search/
│   ├── 02_selection_sort/
│   ├── 03_recursion/
│   ├── 04_divide_and_conquer/
│   └── 05_graphs/
├── elements_of_programming_interviews/
│   └── <NN>_<chapter>/<X.Y>_<section>/<problem>.py, variant_<problem>.py
├── run_tests.py
└── README.md
```

## Problem file template

Each `.py` problem file has the same four parts:

1. **Module docstring:** the problem, constraints, a "How it works" outline, and worked examples.
2. **`class Solution`** (or a named class for data-structure problems), with typed method stubs marked `# TODO` and docstrings giving time and space complexity.
3. **`test_<name>()`:** `assert`-based cases that print `✓ Test N passed` and end with `✅ All tests passed!`.
4. **`if __name__ == "__main__":`**, which runs the tests.

Workflow: replace the `# TODO` stub with your solution, run the file until all tests pass, then commit (`feat: Add <problem> ...`).

## Running

Run one problem:

```bash
python3 fundamentals/01_binary_search/binary_search.py
```

Run everything, or any folder, and get a progress summary:

```bash
python3 run_tests.py                                         # whole repo
python3 run_tests.py elements_of_programming_interviews/05_arrays
python3 run_tests.py fundamentals -v                         # list each file
python3 run_tests.py --show-failures                         # show errors for failing files
python3 run_tests.py fundamentals --logs                     # print each file's full output
```

Running a single file through `run_tests.py` always prints its full output.

Each file is reported as one of:

| Status | Meaning |
|---|---|
| PASS | All tests passed |
| TODO | Still has a `# TODO` stub (not attempted yet) |
| FAIL | No `# TODO` left, but tests fail (attempted solution is wrong) |
| TIMEOUT | Took longer than the timeout (default 30s) |

`run_tests.py` exits with status 1 only on FAIL or TIMEOUT, so unattempted stubs never break a run. Requires Python 3.8+ and no third-party packages.
