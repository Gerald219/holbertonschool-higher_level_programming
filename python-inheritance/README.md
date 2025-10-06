# Python - Inheritance  
<p align="center">
  <img src="https://img.shields.io/badge/Holberton_Project-Python_Inheritance-blue?logo=python&logoColor=white&style=for-the-badge"/>
</p>

---

## Description  
This project teaches how **inheritance** works in Python — how one class can reuse, extend, or change the behavior of another.  
It’s like families: a **child class** inherits traits from its **parent class**, but can still have its own unique features.  

Through each task, you learn how to:
- Create subclasses from existing classes  
- Override methods  
- Validate values and attributes  
- Use `super()` to call parent methods  
- Understand special methods like `__eq__`, `__ne__`, and `__str__`  
- Add new attributes safely  
- Use built-in functions like `isinstance()`, `issubclass()`, and `type()`  

---

## Learning Objectives (simplified)
- A **superclass** (or parent class) is the base where attributes and methods start.  
- A **subclass** (or child class) inherits behavior from a parent.  
- An **instance** can only get new attributes if the class design allows it.  
- The function `super()` lets a subclass call the parent’s version of a method.  
- You can override methods to change behavior without rewriting everything.  
- Functions like `isinstance()` and `issubclass()` check relationships between classes.  

---

##  Tasks Summary  

### **0. Lookup**  
Function that returns a list of all attributes and methods inside an object.  
 *Like peeking into an object’s backpack to see what tools it carries.*  

---

### **1. My List**  
A class that inherits from `list` and prints the list in sorted order.  
 *Takes a messy pile of numbers and prints them neatly organized.*  

---

### **2. Exact Same Object**  
Checks if an object is **exactly** the same class type.  
 *Like asking: are you my identical twin?*  

---

### **3. Same Class or Inherit From**  
Checks if an object is an instance of a class **or any of its children**.  
 *Like asking: are you part of my family line?*  

---

### **4. Only Subclass Of**  
Checks if an object inherits from a class **but is not the same type**.  
 *A child of a parent, but not the parent itself.*  

---

### **5. Geometry Module**  
Creates an empty `BaseGeometry` class — a simple starting point for geometry shapes.  
 *It’s like a blank canvas waiting for more geometric logic.*  

---

### **6. Improve Geometry**  
Adds an `area()` method that raises an error — forcing future classes to define their own area.  
 *A reminder saying “Hey! You need to fill in this formula yourself.”*  

---

### **7. Integer Validator**  
Adds `integer_validator()` to check if a value is a positive integer.  
 *Makes sure any shape built later has proper, positive side lengths.*  

---

### **8. Rectangle**  
Creates a `Rectangle` that inherits from `BaseGeometry`.  
Uses `integer_validator()` to check width and height before saving them.  
 *Builds a real geometric shape from the base rules.*  

---

### **9. Full Rectangle**  
Extends the Rectangle to calculate `area()` and display `[Rectangle] width/height`.  
 *Now the rectangle can show its size and describe itself properly.*  

---

### **10. Square #1**  
Creates a `Square` from the `Rectangle`, validating that both sides are equal.  
 *A special rectangle that keeps both sides perfectly even.*  

---

### **11. Square #2**  
Square borrows all the tools from the Rectangle class, checks that the size is a valid number, tells the Rectangle parent to make both sides equal, quietly keeps that size stored inside itself, and when you print it, it simply shows `[Square] size/size` so you know it’s a perfect square.  

---

### **12. MyInt (The Rebel Integer)**  
MyInt class borrows all the behavior from `int` but acts like its rebel twin, flipping `==` (equal to) and `!=` (not equal to), so when you say they’re equal it says no, and when you say they’re not it says yes.  

---

### **13. Can I?**  
add_attribute() acts like a helper that checks if an object can hold a new name tag using `hasattr()`, adds it with `setattr()`, or raises `TypeError` if it can’t.  
 *It’s like asking “can I stick this label here?” — if yes, it stays; if not, it falls off.*  

---

##  Key Functions Learned
| Function | What It Does | Simple Description |
|-----------|---------------|--------------------|
| `super()` | Calls parent class methods | Like asking your parent to help finish a task |
| `isinstance()` | Checks if something belongs to a class | “Is this a type of that?” |
| `issubclass()` | Checks if one class inherits from another | “Is this class a child of that one?” |
| `hasattr()` | Checks if an object has a specific property | “Do you have this pocket?” |
| `setattr()` | Adds or changes an attribute dynamically | “Let me stick this label on you.” |
| `__eq__`, `__ne__` | Define equality and inequality behavior | Control how “==” and “!=” respond |
| `__str__()` | Defines what prints when you use `print()` | Lets objects describe themselves clearly |

---

