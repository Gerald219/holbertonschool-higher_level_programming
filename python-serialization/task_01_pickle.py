#!/usr/bin/env python3
"""Task 1 - serialize/deserialize a custom object using pickle."""


import pickle  # save & load full Python objects to/from files


class CustomObject:
    """Object with basic info: name (str), age (int), is_student (bool)."""

    def __init__(self, name, age, is_student):
        self.name = name  # person's name
        self.age = age  # person's age
        self.is_student = is_student  # student status

    def display(self):
        """Print data in required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Save this object to filename using pickle.
        """
        try:
            with open(filename, "wb") as f:  # wb = write binary
                pickle.dump(self, f)  # write this object into file
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load object from filename using pickle.
        """
        try:
            with open(filename, "rb") as f:  # rb = read binary
                obj = pickle.load(f)  # read object from file
            if isinstance(obj, cls):  # confirm type is CustomObject
                return obj
            return None
        except Exception:
            return None
