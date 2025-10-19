#!/usr/bin/python3
"""Student class that can export and reload its data."""


class Student:
    """Defines a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize student with name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the student."""
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attributes using the given dictionary."""
        # look at every item in the dictionary
        for key, value in json.items():
            # change the student's data to match the dictionary
            setattr(self, key, value)
