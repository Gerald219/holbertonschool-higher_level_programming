#!/usr/bin/python3
"""Basegeometry class with area and integers validation"""


class BaseGeometry:
    """Base class for geometry shapes."""

    def area(self):
        """Raise an exception because area has no content"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if value is a positive integer, method inside a class"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")