#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry-related operations."""

    def area(self):
        """Raises an Exception indicating that area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is a positive integer.

        Args:
            name (str): the name of the value (used in error messages)
            value (int): the value to validate

        Raises:
            TypeError: if 'value' is not an integer
            ValueError: if 'value' is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
