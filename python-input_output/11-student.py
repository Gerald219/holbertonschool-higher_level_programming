#!/usr/bin/python3
"""Defines a class Student that can be saved and reloaded from JSON."""


class Student:
    """Student class with attributes and JSON conversion tools."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary version of the instance.
        If attrs is a list of strings, only return those keys.
        """
        if (isinstance(attrs, list) and
                all(isinstance(ele, str) for ele in attrs)):
            return {k: getattr(self, k)
                    for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Update attributes from a dictionary."""
        for k, v in json.items():
            setattr(self, k, v)
