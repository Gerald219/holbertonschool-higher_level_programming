#!/usr/bin/python3
"""
This module defines add_integer function to safely add two numbers.
"""

def add_integer(a, b=98):
    """
    Adds two numbers after checking if they are valid ints or floats.
    Casts floats to ints. Rejects strings, NaN, or inf values.
    """
    if not isinstance(a, (int, float)) or a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
