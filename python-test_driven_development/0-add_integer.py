#!/usr/bin/python3
"""
0-add_integer module
Defines a function that adds two numbers after validating them.
"""


def add_integer(a, b=98):
    """
    Add two numbers as integers.

    Args:
        a: first number (int or float).
        b: second number (int or float, default 98).

    Returns:
        int: sum of a and b as integers.

    Raises:
        TypeError: if a or b is not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

