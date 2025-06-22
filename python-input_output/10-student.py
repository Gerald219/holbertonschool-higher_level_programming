#!/usr/bin/python3
"""Student class with selective to_json method"""


class Student:
    """Defines a student by first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary with selected keys if attrs is a list,
        otherwise returns all attributes."""
        if type(attrs) == list and all(type(attr) == str for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
