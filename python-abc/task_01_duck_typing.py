#!/usr/bin/env python3
"""Defines an abstract Shape class and its subclasses Circle and Rectangle, demonstrating duck typing."""


from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for geometric shapes."""
    pass
class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass

