#!/usr/bin/python3
"""
This module defines add_integer function to safely add two numbers.
"""

def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if isinstance(a, float):
        if a != a or a == float('inf') or a == float('-inf'):
            raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(b, float):
        if b != b or b == float('inf') or b == float('-inf'):
            raise TypeError("b must be an integer")

    return int(a) + int(b)
