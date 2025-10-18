<!-- anchor for "back to top" -->
<a id="readme-top"></a>

<p align="center">
  <a href="#readme-top">
    <img alt="Assignment: Python — Input/Output" src="https://img.shields.io/badge/Assignment-Python%20--%20Input%2FOutput-blue">
  </a>
  <a href="#task-function-glossary">
    <img alt="Tasks: 15" src="https://img.shields.io/badge/Tasks-15-6c757d">
  </a>
</p>

---

# Python — Input/Output

This project teaches how Python interacts with files and data.  
You’ll learn how to **open, read, write, append, and save data**, and how to convert Python objects into JSON so your programs can “remember” information.  

---

## What You’ll Learn

- Opening and closing files safely  
- Reading a file all at once or line by line  
- Writing and appending text to files  
- Using `with` to manage files automatically  
- Understanding JSON: saving and loading structured data  
- Handling command-line arguments with `sys.argv`  
- Serializing and deserializing Python objects  

---

<a id="task-function-glossary"></a>

## Task Function Summaries — function, definition, and result

### 0) Read file  
**File:** `0-read_file.py`  
- **What it does:** Reads a UTF-8 text file and prints its content.  
- **Main idea:** Learn to open and read safely with a `with` block.  
- **Result:** File content printed exactly as it is.  

---

### 1) Write to a file  
**File:** `1-write_file.py`  
- **What it does:** Writes text to a file and returns how many characters were written.  
- **Main idea:** Use `"w"` mode to write (and overwrite).  
- **Result:** File created or replaced with new content.  

---

### 2) Append to a file  
**File:** `2-append_write.py`  
- **What it does:** Adds text to the end of a file and returns how many characters were added.  
- **Main idea:** Use `"a"` mode to add new content without deleting old text.  
- **Result:** Existing file grows with every run.  

---

### 3) To JSON string  
**File:** `3-to_json_string.py`  
- **What it does:** Converts a Python object (like a dict or list) into a JSON string.  
- **Main idea:** Learn JSON serialization with `json.dumps()`.  
- **Result:** Returns a string version ready to save.  

---

### 4) From JSON string to Object  
**File:** `4-from_json_string.py`  
- **What it does:** Turns a JSON string back into a Python object.  
- **Main idea:** Deserialize using `json.loads()`.  
- **Result:** You get your original Python data back.  

---

### 5) Save Object to a file  
**File:** `5-save_to_json_file.py`  
- **What it does:** Saves a Python object into a file as JSON.  
- **Main idea:** Combine writing with serialization.  
- **Result:** File now contains JSON text that represents your object.  

---

### 6) Create object from a JSON file  
**File:** `6-load_from_json_file.py`  
- **What it does:** Reads a JSON file and recreates the Python object.  
- **Main idea:** Load + deserialize.  
- **Result:** Python object ready to use again.  

---

### 7) Save & reload — add items  
**File:** `7-add_item.py`  
- **What it does:** Adds command-line arguments to a list, saves them to a file, and reloads them each run.  
- **Main idea:** Combine file I/O, JSON, and command-line inputs.  
- **Result:** A growing list that remembers added items between runs.  

---

### 8) Class to JSON  
**File:** `8-class_to_json.py`  
- **What it does:** Returns the dictionary description of an object for JSON serialization.  
- **Main idea:** Learn to prepare class instances for saving.  
- **Result:** Dictionary version of the object’s attributes.  

---

### 9) Student to JSON  
**File:** `9-student.py`  
- **What it does:** Defines a `Student` class that can return its JSON dictionary.  
- **Main idea:** Combine classes and serialization.  
- **Result:** Student data easily saved and restored.  

---

### 10) Student to JSON with filter  
**File:** `10-student.py`  
- **What it does:** Returns selected attributes of a `Student` when exporting.  
- **Main idea:** Learn attribute filtering.  
- **Result:** Cleaner, customized JSON output.  

---

### 11) Student to disk and reload  
**File:** `11-student.py`  
- **What it does:** Extends `Student` to load data from JSON, restoring attributes.  
- **Main idea:** Full round trip — save and load class instances.  
- **Result:** Object persistence.  

---

### 12) Pascal’s Triangle  
**File:** `12-pascal_triangle.py`  
- **What it does:** Generates Pascal’s triangle as a list of lists.  
- **Main idea:** Work with nested lists and math patterns.  
- **Result:** Returns Pascal’s triangle of size `n`.  

---

### 13) Search and update  
**File:** `100-append_after.py`  
- **What it does:** Inserts a new line of text after each line containing a specific string.  
- **Main idea:** Read + modify files dynamically.  
- **Result:** Updated text file with conditional inserts.  

---

### 14) Log parsing  
**File:** `101-stats.py`  
- **What it does:** Reads from `stdin`, processes log lines, and computes running statistics (file size, status codes).  
- **Main idea:** Handle streaming input and dynamic calculation.  
- **Result:** Displays updated statistics during runtime.  

---

### 15) Advanced — optional exploration  
**What it does:** Integrates all the concepts into more complex data manipulation and serialization.  
- **Main idea:** Apply everything — read, write, append, JSON, classes, and error handling together.  

---

## Requirements

- Python 3.8.5 on Ubuntu 20.04 LTS  
- All files executable (`chmod +x`)  
- Code passes `pycodestyle` 2.7.*  
- Every function, class, and module includes documentation  

---

## Why It iss Useful

File I/O is one of the most practical parts of Python.  
Everything from saving user settings, keeping a game’s score, or reading configuration files depends on these skills.  
After this project, you’ll know how to make your programs **remember, store, and share data**.

---
