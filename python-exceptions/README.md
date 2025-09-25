
<!-- anchor for "back to top" -->
<a id="readme-top"></a>

<p align="center">
  <a href="#readme-top">
    <img alt="Assignment: Python — Exceptions" src="https://img.shields.io/badge/Assignment-Python%20—%20Exceptions-blue">
  </a>
  <a href="#task-function-glossary">
    <img alt="Tasks: 7" src="https://img.shields.io/badge/Tasks-7-6c757d">
  </a>
</p>

---

# Python — Exceptions

Short description: handling what exceptions are, how to catch them, how to always run cleanup, and how to raise clear errors by choice.

## Key topics
- Errors vs. exceptions
- try / except / else / finally
- Printing exact messages and returning safe values
- Raising built-in exceptions (TypeError, NameError)
- Cleanup that always runs (finally)

---

## Task summaries — simple wording <a id="task-function-glossary"></a>

### 0) Safe list printing
- What it does: Tries to print the first x items of a list on one line. Doesn’t crash if the list is shorter. Returns how many items were actually printed.
- Function: safe_print_list(my_list=[], x=0) → int
- Result: Prints the items that exist; returns the count printed.

---

### 1) Safe printing of an integer
- What it does: Tries to print a value as an integer using "{:d}". If it isn’t an integer, nothing is printed and the function reports False.
- Function: safe_print_integer(value) → bool
- Result: Prints the number and returns True for ints; returns False for anything else.

---

### 2) Print and count integers
- What it does: Looks at the first x items in a list, prints only the ones that are integers (quietly skips others). Returns how many integers were printed.
- Function: safe_print_list_integers(my_list=[], x=0) → int
- Result: Only integers are shown; asking past the list size can raise IndexError (as the task expects).

---

### 3) Integers division with debug
- What it does: Divides a by b. Always prints “Inside result: <number or None>” in finally. Returns the division result or None if it can’t divide.
- Function: safe_print_division(a, b) → float | None
- Result: Normal case returns a float; divide-by-zero returns None and still prints the message.

---

### 4) Divide a list
- What it does: Divides items from two lists, position by position, up to list_length. Builds and returns a new result list. Prints short messages when something is wrong.
- Function: list_division(my_list_1, my_list_2, list_length) → list
- Result: Each spot is the division value, or 0 on problems. Messages used: “wrong type”, “division by 0”, “out of range”.

---

### 5) Raise exception
- What it does: Always raises a TypeError on purpose.
- Function: raise_exception() → None
- Result: Caller receives a TypeError to handle.

---

### 6) Raise a message
- What it does: Raises a NameError with a message you pass in.
- Function: raise_exception_msg(message="") → None
- Result: Caller gets a NameError that includes your message.

