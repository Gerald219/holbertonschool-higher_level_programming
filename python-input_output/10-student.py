#!/usr/bin/python3
"""Student class that can show itself as json format dictionary."""


class Student:
    """Defines a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """initialize student with name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        # method start
        """Return a dictionary representation of the student."""
        # check list
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            # filter keys
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        # return all
        return self.__dict__.copy()
