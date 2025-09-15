<a id="readme-top"></a>
<div align="center">
  <a href="#readme-top">
    <img alt="Assignment: Python — More Data Structures" src="https://img.shields.io/badge/Assignment-Python%20--%20More%20Data%20Structures%3A%20Set%2C%20Dictionary-blue">
  </a>
  <a href="#task-function-glossary">
    <img alt="Tasks: 16" src="https://img.shields.io/badge/Tasks-16-6c757d">
  </a>
</div>

---

# Python — More Data Structures: Set, Dictionary

Intro module on **sets**, **dictionaries**, and small functional tools:
`lambda`, `map`, `filter`, `reduce`. We also keep code clean with
**pycodestyle** and the **79-char** rule.

## How I check my files
- `pycodestyle file.py` → checks Python style rules.
- `wc -l file.py` → shows line count.
- `wc -L file.py` → shows longest line (confirm ≤ 79 chars).

---

## 0) Squared simple — `0-square_matrix_simple.py`
- **What it does:** Returns a **new matrix** with every number squared.
- **Core code you’ll see:** nested `for` loops, `x * x`.
- **In plain words:** Make a copy of the grid and replace each number with number × itself.
- **Prototype:** `def square_matrix_simple(matrix=[]):`

## 1) Search and replace — `1-search_replace.py`
- **What it does:** Builds a **new list** where every match of `search`
  is replaced with `replace`.
- **Core code:** `for`, `==`, `list.append`.
- **In plain words:** Walk the list; if an item equals the target, swap it; otherwise keep it.

## 2) Unique addition — `2-uniq_add.py`
- **What it does:** Adds each integer **once** (ignores duplicates).
- **Core code:** `set()`, `.add`, `sum`.
- **In plain words:** Drop duplicates with a set, then add the remaining numbers.

## 3) Present in both — `3-common_elements.py`
- **What it does:** Returns elements **common** to both sets.
- **Core code:** set intersection `&`.
- **In plain words:** Keep only things that appear in **both** bags.

## 4) Only differents — `4-only_diff_elements.py`
- **What it does:** Returns elements in **exactly one** of the sets.
- **Core code:** set symmetric difference `^`.
- **In plain words:** Keep things that are **not shared**.

## 5) Number of keys — `5-number_keys.py`
- **What it does:** Counts how many **keys** a dict has.
- **Core code:** `len(a_dictionary)`.
- **In plain words:** How many labels are in the box.

## 6) Print sorted dictionary — `6-print_sorted_dictionary.py`
- **What it does:** Prints `key: value` pairs by **alphabetical key**.
- **Core code:** `sorted(a_dictionary)`, f-strings.
- **In plain words:** Sort the labels, then print each label with what it holds.

## 7) Update dictionary — `7-update_dictionary.py`
- **What it does:** **Adds** a new `key: value` or **replaces** value if key exists.
- **Core code:** `a_dictionary[key] = value`.
- **In plain words:** If the label exists, change its content; if not, create it.

## 8) Simple delete by key — `8-simple_delete.py`
- **What it does:** Deletes a `key` if present; otherwise leaves dict unchanged.
- **Core code:** `if key in a_dictionary`, `del a_dictionary[key]`.
- **In plain words:** If the label is there, remove the label and its content.

## 9) Multiply by 2 — `9-multiply_by_2.py`
- **What it does:** Returns a **new dict** with all **values × 2** (same keys).
- **Core code:** `.items()`, new dict assignment, `v * 2`.
- **In plain words:** Copy the labels; double what each label stores.

## 10) Best score — `10-best_score.py`
- **What it does:** Returns the **key with the largest value**; `None` if empty.
- **Core code:** `max(a_dictionary, key=a_dictionary.get)`.
- **In plain words:** Pick the label whose number is the biggest.

## 11) Multiply by using map — `11-multiply_list_map.py`
- **What it does:** Returns a **new list** with each value **× number**; no loops.
- **Core code:** `map`, `lambda`, `list(...)`.
- **In plain words:** Apply “x × number” to every item using `map` and a tiny function.
- **Note:** File must be **max 3 lines** (no inline comments).

## 12) Roman to Integer — `12-roman_to_int.py`
- **What it does:** Converts a **Roman numeral** string to an **integer**.
- **Core code:** dict lookup, `reversed`, compare `value < prev`, add/subtract.
- **In plain words:** Walk right→left; add numbers, but subtract if a smaller comes before a bigger (like `IV` = 4).

## 13) Weighted average! — `100-weight_average.py`
- **What it does:** Returns the **weighted average** of `(score, weight)` tuples.
- **Core code:** loop, `score * weight`, `sum of weights`, divide.
- **In plain words:** Multiply each score by its weight, add all, then divide by total weight.

## 14) Squared by using map — `101-square_matrix_map.py`
- **What it does:** Squares every number in a **matrix** using `map` (no loops).
- **Core code:** nested `map`, `lambda x: x * x`, `list(...)`.
- **In plain words:** For each row, square each number with `map`. Return a new matrix.
- **Note:** File must be **max 3 lines**.

## 15) Delete by value — `102-complex_delete.py`
- **What it does:** Deletes **all keys** in a dict whose **value equals** the given one.
- **Core code:** loop over `a_dictionary.items()`, collect keys, then `del` each.
- **In plain words:** Find every label that stores the target value and remove those labels.

---

## Task Function Glossary
Quick peek at the exact tools used across tasks:

- **Lists / Loops:** `for`, `append`, list literals `[]`
- **Sets:** `set()`, `&` (intersection), `^` (symmetric difference)
- **Dicts:** `.items()`, indexing `dict[key]`, `del`, `len(dict)`, `sorted(dict)`
- **Math / Helpers:** `x * x` (square), `sum`, `max(..., key=...)`
- **Map/Functional:** `map`, `lambda`, `list(map(...))`
- **Strings / Roman:** `reversed(s)`, dict lookup `roman_map.get(ch, 0)`

---

## Notes on style and execution
- First line in every file: `#!/usr/bin/python3`
- Make files executable: `chmod +x file.py`
- Style check: `pycodestyle file.py`
- Length check: `wc -l file.py` and `wc -L file.py` (longest line ≤ 79)
- Some tasks enforce a **max 3 lines** file; keep comments in the README.

---
