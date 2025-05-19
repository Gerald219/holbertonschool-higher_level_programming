#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (converted to integers).

    Args:
        a (int or float): First number.
        b (int or float, default=98): Second number.

    Returns:
        int: The sum of a and b as integers.

    Raises:
        TypeError: If a or b are not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")  # ❗️Fulfills test: None input

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")  # ❗️Fulfills test: string input

    return int(a) + int(b)  # Cast float -> int before adding
