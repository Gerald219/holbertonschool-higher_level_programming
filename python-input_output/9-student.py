#!/usr/bin/python3
"""Defines a Student class for JSON serialization."""


class Student:
    """Student class with public attributes."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary description for JSON serialization."""
        return self.__dict__
