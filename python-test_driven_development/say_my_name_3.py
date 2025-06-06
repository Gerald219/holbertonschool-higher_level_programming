#!/usr/bin/python3
"""
This module defines a function that prints a full name.
"""


def say_my_name(first_name=None, last_name=""):
    """
    Prints: My name is <first_name> <last_name>
    Raises TypeError if inputs are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
