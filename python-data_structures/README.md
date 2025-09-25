<!-- anchor for "back to top" -->
<a id="readme-top"></a>

<p align="center">
  <img alt="Assignment: Python — Data Structures: Lists, Tuples" src="https://img.shields.io/badge/Assignment-Python%20--%20Data%20Structures%3A%20Lists%2C%20Tuples-blue">
  <img alt="Tasks: 13" src="https://img.shields.io/badge/Tasks-13-6c757d">
  <img alt="Level: Novice" src="https://img.shields.io/badge/Level-Novice-success">
  <img alt="Python: 3.8.5" src="https://img.shields.io/badge/Python-3.8.5-yellow">
  <img alt="OS: Ubuntu 20.04" src="https://img.shields.io/badge/OS-Ubuntu%2020.04-orange">
  <img alt="Style: pycodestyle 2.7" src="https://img.shields.io/badge/Style-pycodestyle%202.7-9cf">
</p>

<h1 align="center">Python — Data Structures: Lists, Tuples</h1>

<p align="center"><em>Learn lists and tuples, the basic tools to add, change, remove, find, and combine items—plus quick list builds, pack/unpack, and delete.</em></p>

---

## Quick view

- Lists: ordered, changeable, can grow/shrink  
- Tuples: ordered, fixed once made  
- Strings vs lists: both ordered; strings can’t be changed, lists can  
- Use lists for stacks (append/pop) and queues (append/pop at ends)  
- Build lists fast with list comprehensions  
- Pack items into a tuple; unpack them into variables  
- Delete items or ranges with `del`

### Lists vs Tuples (tiny guide)

| Feature         | List (e.g., [1, 2, 3]) | Tuple (e.g., (1, 2, 3)) |
|---|---|---|
| Change items?   | Yes                    | No                      |
| Add/remove?     | Yes (append, pop …)    | No                      |
| Use case        | Data that changes      | Fixed pairs/records     |
| Memory/safety   | Heavier, flexible      | Lighter, stable         |

---

## Quick reference (lists)

| Action | How it’s used | What it does |
|---|---|---|
| append(x) | my_list.append(x) | add to the end |
| extend(L) | my_list.extend(L) | add many to the end |
| insert(i,x) | my_list.insert(i, x) | put x at index i |
| remove(x) | my_list.remove(x) | delete first x |
| pop() / pop(i) | my_list.pop() | take and return last (or at i) |
| clear() | my_list.clear() | make list empty |
| index(x) | my_list.index(x) | where x first appears |
| count(x) | my_list.count(x) | how many x |
| sort() | my_list.sort() | sort in place |
| reverse() | my_list.reverse() | flip order |
| copy() | new = my_list.copy() | shallow copy |

**Pack/Unpack:** `a, b = (1, 2)` and swap as `a, b = b, a`  
**Delete:** `del my_list[i]` or `del my_list[1:3]`

---

<a id="task-function-glossary"></a>
## Tasks — short cards

### 0) Print a list of integers
- Does: print each number on its own line using str.format  
- Learn: simple loop + formatting  
- Output: one number per line

---

### 1) Secure access to an element in a list
- Does: return the element at index; if index is negative or too big, return None  
- Learn: safe indexing without try/except  
- Output: found item or None

---

### 2) Replace element
- Does: change the item at index; if index is bad, return the original list unchanged  
- Learn: in-place update with bounds check  
- Output: updated list (or original)

---

### 3) Print a list of integers… in reverse
- Does: print the list from end to start, one number per line  
- Learn: reverse order printing  
- Output: last-to-first lines

---

### 4) Replace in a copy
- Does: return a new list with one place changed; original stays the same  
- Learn: copy-then-change pattern  
- Output: new list and original unchanged

---

### 5) Can you C me now?
- Does: return text without the letters c and C  
- Learn: build a new string by skipping unwanted chars  
- Output: filtered text

---

### 6) Lists of lists = Matrix
- Does: print a matrix row by row with spaces between numbers  
- Learn: nested loops + formatting rules  
- Output: neatly spaced grid

---

### 7) Tuples addition
- Does: add two 2-item tuples; missing spots use 0; ignore extras  
- Learn: tuple access with defaults  
- Output: new tuple like (a1+b1, a2+b2)

---

### 8) More returns!
- Does: return a pair (length, first_char) or (length, None) if empty  
- Learn: return multiple values  
- Output: two-item tuple

---

### 9) Find the max
- Does: return the biggest number or None if the list is empty  
- Learn: scan and keep the best so far  
- Output: max value or None

---

### 10) Only by 2
- Does: return a list of True/False marking which numbers are even  
- Learn: per-item test mapped to a new list  
- Output: booleans, same length as input

---

### 11) Delete at
- Does: remove the item at index; if the index is bad, do nothing  
- Learn: use del without pop  
- Output: list with that item gone (or unchanged)

---

### 12) Switch
- Does: swap a and b in one line  
- Learn: multiple assignment for swapping  
- Output: values switched

---

<p align="right"><a href="#readme-top">back to top ⤴</a></p>
