#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())     # Bark
print(garfield.sound())  # Meow

animal = Animal()
print(animal.sound())    # Should raise TypeError
