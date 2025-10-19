#!/usr/bin/python3
"""Student class that can present itself as JSON."""


class Student:
    """Makes a student with name and age, dictionary."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        # returns all the data about this student
        return self.__dict__
