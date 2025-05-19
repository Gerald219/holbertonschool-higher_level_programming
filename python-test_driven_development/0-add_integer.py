#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""

import math  # used to detect NaN or infinity values

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
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and (math.isnan(a) or math.isinf(a)):
        raise TypeError("a must be an integer")

    if isinstance(b, float) and (math.isnan(b) or math.isinf(b)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
