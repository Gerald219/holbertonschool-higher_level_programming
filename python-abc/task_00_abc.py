#!/usr/bin/env python3
"""Defines an abstract Animal class and its subclasses."""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by all subclasses."""
        pass


class Dog(Animal):
    """Dog class that implements the Animal interface."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class that implements the Animal interface."""

    def sound(self):
        return "Meow"
