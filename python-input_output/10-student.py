#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student with name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary of student attributes"""
        if isinstance(attrs, list) and all(type(elem) is str for elem in attrs):
            return {key: self.__dict__[key] for key in attrs if key in self.__dict__}
        return self.__dict__
