<!-- anchor for "back to top" -->
<a id="readme-top"></a>

<p align="center">
  <a href="#readme-top">
    <img alt="Assignment: ChatGPT - Introduction" src="https://img.shields.io/badge/Assignment-ChatGPT%20--%20Introduction-blue">
  </a>
  <a href="#task-function-glossary">
    <img alt="Tasks: 6" src="https://img.shields.io/badge/Tasks-6-6c757d">
  </a>
</p>

---

# ChatGPT – Introduction

### Module on AI-assisted coding focused on debugging and automation.
ChatGPT helps find bugs, explain causes, propose small fixes verified with simple tests, and automate repeat steps. The result is faster work and fewer mistakes, with all AI output reviewed before use.

## PROJECT 1

This project covers:

- **Debugging** — finding and fixing mistakes so code behaves as intended.
- **Automation** — making the computer handle repetitive steps automatically.
- **Enhanced Debugging Skills** — clearly identify problems and apply AI to implement effective fixes.
- **Automation Proficiency** — use AI to create repeatable workflows to run tests, format code, and update docs for consistent files and fewer errors.


## Task Function Summaries - function, definition, result.



### 0) Debugging — Python Factorial
- **What it does:** Makes one big multiplication using all whole numbers from **n** down to **1**.
  *Example: if n = 5 → 5 × 4 × 3 × 2 × 1 = 120.*
- **Function learned/applied:** `factorial(n: int) -> int`
- **Result obtained:** `factorial(5) → 120` · `factorial(0) → 1`
---

### 1) Debugging — Python Arguments
- **What it does:** Prints only the values passed on the command line, excluding the script’s filename.
  *Example: run `./print_arguments.py 1 2 3` → prints `1`, `2`, `3` on separate lines.*
- **Function learned/applied:** `args_only(argv: list[str]) -> list[str]`
- **Result obtained:** `["print_arguments.py","1","2","3"]` → `1` · `2` · `3`
---

### 2) Debugging — HTML / Javascript
- **What it does:** Changes the background color randomly when the button is clicked.
- **Fix needed:** button ID mismatch (`colorButon` vs `colorButton`).
- **Fix applied:** Make the button’s id match the JS listener.
- **Result obtained:** Background changes on every click.

---
### 3) Debugging — Python Mines
- **What it does:** Runs a console Minesweeper game where you reveal cells while avoiding mines.
  *Example: keep revealing safe cells until all non-mine tiles are open.*
- **Fix needed:** Detect when all non-mine cells have been revealed and declare a win.
- **Function learned/applied:** Check win condition by verifying every non-mine cell is revealed.
- **Result obtained:** When all safe cells are revealed, the game prints “Congratulations! You’ve won the game.”

---
### 4) Documentation — Python Factorial
- **What it does:** Calculates the factorial of a number using recursion.
  *Example: `factorial(4)` → `24`.*
- **Fix needed:** Add documentation with three sections: function description, parameters, and returns.
- **Function documented:** `factorial(n: int) -> int`
- **Result obtained:** Function now includes a docstring covering description, parameters, and return value.

---
### 5) Error Handling — Python Checkbook
- **What it does:** Manages a simple checkbook with deposit, withdraw, and balance operations.
  *Example: user types `deposit`, then an amount to add to the balance.*
- **Fix needed:** Prevent crashes when the user enters a non-numeric amount.
- **Function learned/applied:** Input validation with `try/except ValueError` around `float(...)` (apply in both deposit and withdraw).
- **Result obtained:** Invalid amounts show a friendly message and the loop continues without crashing.

---
### 6) Debugging — Tic Tac Toe Python
- **What it does:** 2-player Tic Tac Toe on a 3×3 grid.
- **Fixes needed:** Validate input (numbers and bounds); announce the real winner.
- **Function learned/applied:** Use `try/except` for `input()`, check row/col in {0,1,2}, compute winner after loop.
- **Result obtained:** Bad inputs are ignored; board remains valid; correct winner is printed.

---




geraldlinked@Linkedboy:~/holbertonschool-higher_level_programming$ cat README.md
<!-- anchor for "back to top" -->
<a id="readme-top"></a>

<p align="center">
  <a href="#readme-top">
    <img alt="Assignment: ChatGPT - Introduction" src="https://img.shields.io/badge/Assignment-ChatGPT%20--%20Introduction-blue">
  </a>
  <a href="#task-function-glossary">
    <img alt="Tasks: 6" src="https://img.shields.io/badge/Tasks-6-6c757d">
  </a>
</p>

---

# ChatGPT – Introduction

### Module on AI-assisted coding focused on debugging and automation.
ChatGPT helps find bugs, explain causes, propose small fixes verified with simple tests, and automate repeat steps. The result is faster work and fewer mistakes, with all AI output reviewed before use.

## PROJECT 1

This project covers:

- **Debugging** — finding and fixing mistakes so code behaves as intended.
- **Automation** — making the computer handle repetitive steps automatically.
- **Enhanced Debugging Skills** — clearly identify problems and apply AI to implement effective fixes.
- **Automation Proficiency** — use AI to create repeatable workflows to run tests, format code, and update docs for consistent files and fewer errors.


## Task Function Summaries - function, definition, result.



### 0) Debugging — Python Factorial
- **What it does:** Makes one big multiplication using all whole numbers from **n** down to **1**.
  *Example: if n = 5 → 5 × 4 × 3 × 2 × 1 = 120.*
- **Function learned/applied:** `factorial(n: int) -> int`
- **Result obtained:** `factorial(5) → 120` · `factorial(0) → 1`
---

### 1) Debugging — Python Arguments
- **What it does:** Prints only the values passed on the command line, excluding the script’s filename.
  *Example: run `./print_arguments.py 1 2 3` → prints `1`, `2`, `3` on separate lines.*
- **Function learned/applied:** `args_only(argv: list[str]) -> list[str]`
- **Result obtained:** `["print_arguments.py","1","2","3"]` → `1` · `2` · `3`
---

### 2) Debugging — HTML / Javascript
- **What it does:** Changes the background color randomly when the button is clicked.
- **Fix needed:** button ID mismatch (`colorButon` vs `colorButton`).
- **Fix applied:** Make the button’s id match the JS listener.
- **Result obtained:** Background changes on every click.

---
### 3) Debugging — Python Mines
- **What it does:** Runs a console Minesweeper game where you reveal cells while avoiding mines.
  *Example: keep revealing safe cells until all non-mine tiles are open.*
- **Fix needed:** Detect when all non-mine cells have been revealed and declare a win.
- **Function learned/applied:** Check win condition by verifying every non-mine cell is revealed.
- **Result obtained:** When all safe cells are revealed, the game prints “Congratulations! You’ve won the game.”

---
### 4) Documentation — Python Factorial
- **What it does:** Calculates the factorial of a number using recursion.
  *Example: `factorial(4)` → `24`.*
- **Fix needed:** Add documentation with three sections: function description, parameters, and returns.
- **Function documented:** `factorial(n: int) -> int`
- **Result obtained:** Function now includes a docstring covering description, parameters, and return value.

---
### 5) Error Handling — Python Checkbook
- **What it does:** Manages a simple checkbook with deposit, withdraw, and balance operations.
  *Example: user types `deposit`, then an amount to add to the balance.*
- **Fix needed:** Prevent crashes when the user enters a non-numeric amount.
- **Function learned/applied:** Input validation with `try/except ValueError` around `float(...)` (apply in both deposit and withdraw).
- **Result obtained:** Invalid amounts show a friendly message and the loop continues without crashing.

---
### 6) Debugging — Tic Tac Toe Python
- **What it does:** 2-player Tic Tac Toe on a 3×3 grid.
- **Fixes needed:** Validate input (numbers and bounds); announce the real winner.
- **Function learned/applied:** Use `try/except` for `input()`, check row/col in {0,1,2}, compute winner after loop.
- **Result obtained:** Bad inputs are ignored; board remains valid; correct winner is printed.

---



