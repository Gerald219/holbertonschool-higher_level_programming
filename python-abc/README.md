<a id="readme-top"></a>
<div align="center">
  <a href="#readme-top">
    <img alt="Assignment: Python — Abstract Classes, Interfaces & Mixins" src="https://img.shields.io/badge/Assignment-Python%20--%20Abstract%20Classes%2C%20Interfaces%20%26%20Mixins-blue">
  </a>
  <a href="#task-function-glossary">
    <img alt="Tasks: 6" src="https://img.shields.io/badge/Tasks-6-6c757d">
  </a>
</div>

---

# Python — Abstract Classes, Interfaces & Mixins

This project shows how Python handles **abstract base classes**, **interfaces**, and **mixins**.  
It focuses on building class structures that share behavior while keeping code modular and easy to extend.

---

## How I check my files
- `pycodestyle file.py` → check for style errors.
- `wc -l file.py` → count total lines.
- `wc -L file.py` → check the longest line (≤ 79 chars).

---

## 0) ABC Basics — `task_00_abc.py`
- **What it does:** Creates an abstract base class with abstract methods.
- **Key idea:** Classes that inherit must define certain functions.
- **In short:** Like a contract — “if you inherit me, you must fill these methods.”

---

## 1) Duck Typing — `task_01_duck_typing.py`
- **What it does:** Uses duck typing to show behavior-based design.
- **Key idea:** “If it walks like a duck and quacks like a duck, it’s a duck.”
- **In short:** Objects are recognized by what they do, not what they are.

---

## 2) Verbose List — `task_02_verboselist.py`
- **What it does:** Subclasses `list` and prints messages when modified.
- **Key idea:** Shows inheritance and method overriding.
- **In short:** A list that speaks every time it changes.

---

## 3) Counted Iterator — `task_03_countediterator.py`
- **What it does:** Counts how many items have been iterated.
- **Key idea:** Tracks progress through an iterable.
- **In short:** Like a counter that tells you how far you’ve gone in a loop.

---

## 4) Flying Fish — `task_04_flyingfish.py`
- **What it does:** Uses mixins to make a fish that can both swim and fly.
- **Key idea:** Combines small, reusable classes (mixins) into one object.
- **In short:** A fish with two talents — swimming and flying.

---

## 5) The Mystical Dragon — `task_05_dragon.py`
- **What it does:** Combines `SwimMixin` and `FlyMixin` into a `Dragon` class.
- **Key idea:** Mix multiple small abilities into one complete class.
- **In short:** A dragon that swims, flies, and roars.

### Example output:
```bash
$ ./main_05_dragon.py
The creature swims!
The creature flies!
The dragon roars!
