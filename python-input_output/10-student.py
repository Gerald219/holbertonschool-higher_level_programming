#!/usr/bin/python3
"""Defines a Student class with selective JSON representation."""


class Student:
    """Represents a student with basic attributes."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary of selected attributes for JSON serialization."""
        if isinstance(attrs, list):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
