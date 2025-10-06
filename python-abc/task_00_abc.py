#!/usr/bin/env python3
"""Defines abstract Animal class and its subclasses Dog and Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses."""
        pass


class Dog(Animal):
    """Dog class inheriting from Animal."""

    def sound(self):
        """Return the dog's sound."""
        return "Bark! Bark! Woof! Woof!"


class Cat(Animal):
    """Cat class that inherits from Animal."""

    def sound(self):
        """Return the cat's sound."""
        return "Meow Meau! shsh! Purr! Purr!"
