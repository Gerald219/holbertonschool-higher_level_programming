#!/usr/bin/python3

"""
This module adds two integers or floats after checking their types.
"""


def add_integer(a, b=98):
    """
    Adds a and b after converting them to integers.
    Raises TypeError if inputs are not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
