<!-- anchor for "back to top" -->
<a id="readme-top"></a>

<p align="center">
  <img alt="Assignment: Python — import & modules" src="https://img.shields.io/badge/Assignment-Python%20--%20import%20%26%20modules-blue">
  <img alt="Tasks: 10" src="https://img.shields.io/badge/Tasks-10-6c757d">
  <img alt="Level: Novice" src="https://img.shields.io/badge/Level-Novice-success">
  <img alt="Python: 3.10" src="https://img.shields.io/badge/Python-3.10-yellow">
  <img alt="OS: Ubuntu 22.04" src="https://img.shields.io/badge/OS-Ubuntu%2022.04-orange">
  <img alt="Style: pycodestyle 2.7" src="https://img.shields.io/badge/Style-pycodestyle%202.7-9cf">
</p>

<h1 align="center">Python — import & modules</h1>

> TL;DR: Learn to reuse code from other files (modules), list what’s inside with `dir()`, keep scripts from auto-running with `if __name__ == "__main__":`, and read command-line arguments using `sys.argv`.

---

## Mini TOC
- [What you’ll learn](#what-youll-learn)
- [Requirements](#requirements)
- [Tasks](#tasks)

---

## What you’ll learn
- What a module is: a `.py` file you can import to reuse code.
- How to import a function or variable from another file and use it.
- How to make your own module by writing functions and variables in a `.py` file.
- How to list names in a module with `dir(module_name)`.
- How to stop code from running on import using `if __name__ == "__main__":`.
- How to read command-line arguments with `sys.argv` (script name is `argv[0]`).

---

## Requirements
- Ubuntu 22.04, Python 3.10.*
- First line: `#!/usr/bin/python3`
- Files executable, end with a newline
- Follow pycodestyle 2.7.*
- Keep files in `python-import_modules`
- Use `wc` to check length when needed

---

<a id="tasks"></a>
## Tasks

<details>
  <summary>0) Import a simple function from a simple file</summary>

- Does: import `add(a, b)` from add_0.py, set `a = 1`, `b = 2`, print `1 + 2 = 3`.
- Learn: `from add_0 import add`, use variables, format the message, add the main guard.
- Run: `./0-add.py`
- Output: `1 + 2 = 3`
</details>

<details>
  <summary>1) My first toolbox!</summary>

- Does: import `add`, `sub`, `mul`, `div` from calculator_1.py; set `a = 10`, `b = 5`; print all four results.
- Learn: import several names, call each, print in the shown format, add the main guard.
- Run: `./1-calculation.py`
- Output: lines for `+`, `-`, `*`, `/` like `10 + 5 = 15`
</details>

<details>
  <summary>2) How to make a script dynamic!</summary>

- Does: print how many arguments were passed and list them with their position.
- Learn: `import sys`, use `len(sys.argv)`, loop over `argv[1:]`, handle 0, 1, or many.
- Run: `./2-args.py Hello World`
- Output:  
  `2 arguments:`  
  `1: Hello`  
  `2: World`
</details>

<details>
  <summary>3) Infinite addition</summary>

- Does: add all command-line numbers and print the total (0 if none).
- Learn: convert with `int()`, sum `argv[1:]`; big numbers work automatically.
- Run: `./3-infinite_add.py 79 10 -40 -300 89`
- Output: `-162`
</details>

<details>
  <summary>4) Who are you?</summary>

- Does: print all names from hidden_4.pyc, skip names starting with `__`, sort them.
- Learn: `import hidden_4`, `dir(hidden_4)`, filter, sort, print one per line.
- Run (in `/tmp`):  
  `curl -Lso hidden_4.pyc https://github.com/hs-hq/0x02.py/raw/main/hidden_4.pyc`  
  `./4-hidden_discovery.py | sort`
- Output: a sorted list like `my_secret_santa`, `print_hidden`, `print_school`
</details>

<details>
  <summary>5) Everything can be imported</summary>

- Does: import variable `a` from variable_load_5.py and print it.
- Learn: you can import variables, not only functions.
- Run: `./5-variable_load.py`
- Output: `98`
</details>

<details>
  <summary>6) Build my own calculator! (advanced)</summary>

- Does: command-line calculator `./100-my_calculator.py a operator b`
- Learn: check argument count; allow only `+ - * /`; convert to `int`; call the right function; print `<a> <op> <b> = <result>`; exit with code 1 on errors.
- Run:  
  `./100-my_calculator.py 3 + 5` → `3 + 5 = 8`  
  `./100-my_calculator.py` → usage + exit 1
</details>

<details>
  <summary>7) Easy print (advanced)</summary>

- Does: print `#pythoniscool` without using `print`, `eval`, `open`, or `sys`.
- Learn: another output method in ≤ 2 lines (for example, `os.write`).
- Run: `./101-easy_print.py`
- Output: `#pythoniscool`
</details>

<details>
  <summary>8) ByteCode → Python #3 (advanced)</summary>

- Does: write `magic_calculation(a, b)` to match the given bytecode:  
  if `a < b`: `c = add(a, b)`; then for `i` in `range(4, 6)`: `c = add(c, i)`; return `c`.  
  else: return `sub(a, b)`.
- Learn: translate steps into Python and import only what you need.
</details>

<details>
  <summary>9) Fast alphabet (advanced)</summary>

- Does: print `A` to `Z` in one shot (no loops or conditions).
- Learn: use library data, for example `string.ascii_uppercase`.
- Run: `./103-fast_alphabet.py`
- Output: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
</details>

<p align="right"><a href="#readme-top">back to top ⤴</a></p>
