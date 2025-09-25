
<!-- anchor for "back to top" -->
<a id="readme-top"></a>

<p align="center">
  <a href="#readme-top">
    <img alt="Assignment: Python — if/else, loops, functions" src="https://img.shields.io/badge/Assignment-Python%20--%20if%2Felse,%20loops,%20functions-blue">
  </a>
  <a href="#task-function-glossary">
    <img alt="Tasks: 15" src="https://img.shields.io/badge/Tasks-15-6c757d">
  </a>
</p>

---

# Python — if/else, loops, functions

#### Learn: clean indentation; make choices with if/else; repeat work with while/for; skip or stop with continue/break; use else on loops; use pass as a placeholder; count with range; write small functions that return values; know where a variable works (scope) and when a function returns None; read errors from a traceback; do basic math; keep scripts executable and pycodestyle-friendly.

## PROJECT 1

This project covers:

- Indentation — avoid Indentation errors; keep blocks aligned.
- Conditionals — if, elif, else.
- Comments and variables — write notes to adjust the eyes and set values.
- Loops — while and for; use break, continue, loop else; pass does nothing.
- range() — start, stop, step.
- Functions — define, call, return; no return means None; where variables work (scope).
- Traceback — read error messages to fix bugs.
- Arithmetic — +, -, *, /, %, //, **.
- Style and tooling — run with first line #!/usr/bin/python3.

<a id="task-function-glossary"></a>
## Task Function Summaries - function, definition, result.

### 0) Python — if/else, loops, functions — Positive or negative
- **What it does:** Prints a random number and says if it is positive, zero, or negative.  
  *Example: -4 is negative*
- **Function learned/applied:** if / elif / else
- **Result obtained:** <number> is positive | zero | negative
---

### 1) Python — if/else, loops, functions — The last digit
- **What it does:** Prints the last digit of a number with a rule: >5, =0, or <6 and not 0.  
  *Example: Last digit of -626 is -6 and is less than 6 and not 0*
- **Function learned/applied:** modulo %, branching
- **Result obtained:** Last digit of <n> is <d> and is ...
---

### 2) Python — if/else, loops, functions — Alphabet (lowercase)
- **What it does:** Prints abc…z on one line (no extra newline at the end).  
  *Example: abcdefghijklmnopqrstuvwxyz*
- **Function learned/applied:** for + range/chr, print(end="")
- **Result obtained:** abcdefghijklmnopqrstuvwxyz
---

### 3) Python — if/else, loops, functions — Alphabet except q and e
- **What it does:** Prints the lowercase alphabet but skips q and e.  
  *Example: abcdfghijklmnoprstuvwxyz*
- **Function learned/applied:** loop with a simple skip
- **Result obtained:** alphabet without q and e
---

### 4) Python — if/else, loops, functions — Hexadecimal printing
- **What it does:** Prints numbers 0–98 as decimal and hex like d = 0x..  
  *Example: 16 = 0x10*
- **Function learned/applied:** formatting inside a loop
- **Result obtained:** lines from 0 = 0x0 up to 98 = 0x62
---

### 5) Python — if/else, loops, functions — 00…99
- **What it does:** Prints 00 to 99, zero-padded, separated by comma and space, no trailing comma.  
  *Example: 00, 01, 02, … 99*
- **Function learned/applied:** string formatting and last-item handling
- **Result obtained:** one line: 00, 01, 02, … 99
---

### 6) Python — if/else, loops, functions — Two-digit combinations
- **What it does:** Prints all different 2-digit pairs (i < j), sorted, comma and space separated.  
  *Example: 01, 02, … 89*
- **Function learned/applied:** nested loops, ordering, no trailing comma
- **Result obtained:** 01, 02, 03, … 89
---

### 7) Python — if/else, loops, functions — islower(c)
- **What it does:** Returns True if a character is lowercase, else False.  
  *Example: islower('a') → True; islower('H') → False*
- **Function learned/applied:** ord() range check
- **Result obtained:** True or False
---

### 8) Python — if/else, loops, functions — uppercase(str)
- **What it does:** Prints a string in uppercase using a loop (no str.upper).  
  *Example: Best School 98 Battery street → BEST SCHOOL 98 BATTERY STREET*
- **Function learned/applied:** ord()/chr() mapping in a loop
- **Result obtained:** uppercase text printed on one line
---

### 9) Python — if/else, loops, functions — print_last_digit(number)
- **What it does:** Prints the last digit of a number and returns it.  
  *Example: print_last_digit(-1024) prints 4 and returns 4*
- **Function learned/applied:** modulo with negatives, return values
- **Result obtained:** last digit printed, same digit returned
---

### 10) Python — if/else, loops, functions — add(a, b)
- **What it does:** Returns the sum of two numbers.  
  *Example: add(1, 2) -> 3*
- **Function learned/applied:** small function with return
- **Result obtained:** a + b
---

### 11) Python — if/else, loops, functions — pow(a, b)
- **What it does:** Returns a to the power of b.  
  *Example: pow(2, 5) → 32*
- **Function learned/applied:** exponent operator
- **Result obtained:** a ** b
---

### 12) Python — if/else, loops, functions — Fizz Buzz
- **What it does:** Prints 1–100 with Fizz (×3), Buzz (×5), FizzBuzz (×15), space separated.  
  *Example: 1 2 Fizz 4 Buzz … FizzBuzz … 100*
- **Function learned/applied:** branching inside a loop
- **Result obtained:** a single line of tokens separated by spaces
---

### 13) Python — if/else, loops, functions — Smile in the mirror (advanced)
- **What it does:** Prints the alphabet in reverse, switching case each time: zYxW…A.  
  *Example: zYxWvUtSrQpOnMlKjIhGfEdCbA*
- **Function learned/applied:** reverse loop and case toggle
- **Result obtained:** zYxW…A
---

### 14) Python — if/else, loops, functions — Remove at position (advanced)
- **What it does:** Returns the text without the character at index n (out of range → unchanged).  
  *Example: remove_char_at("Best School", 3) → Bes School*
- **Function learned/applied:** build new text as: part before + part after
- **Result obtained:** original text minus the character at position n
---

