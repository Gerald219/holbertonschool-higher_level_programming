#!/usr/bin/python3
"""
Defines class BaseGeometry with area() and integer_validator()
"""


class BaseGeometry:
    """Base class for geometry shapes"""

    def area(self):
        """Not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks that value is a positive integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
