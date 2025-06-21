# Python OOP - Abstract Classes and Inheritance

This project covers advanced Python OOP features: abstract base classes, duck typing, method overriding, mixins, and multiple inheritance. Each task explores a core concept through short, functional class examples.

## Tasks

- **Task 0: Abstract Animal**
  Created an abstract `Animal` class with a `sound()` method. Subclasses `Dog` and `Cat` implement the method.

- **Task 1: Duck Typing**
  Defined `Shape` as an abstract base class, and created `Circle` and `Rectangle` classes that implement `area()` and `perimeter()`.

- **Task 2: VerboseList**
  Extended Python’s `list` to print messages on `append`, `extend`, `remove`, and `pop`.

- **Task 3: CountedIterator**
  Built a custom iterator that tracks how many items were returned during iteration.

- **Task 4: FlyingFish**
  Used multiple inheritance with `Fish` and `Bird`, and created a `FlyingFish` that overrides methods from both.

- **Task 5: Dragon and Mixins**
  Created two mixins (`SwimMixin`, `FlyMixin`) and used them in a `Dragon` class that adds a `roar()` method.

## How to Run

```bash
chmod +x main_*.py
./main_02_verboselist.py
