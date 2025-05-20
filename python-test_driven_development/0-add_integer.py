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
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        if a != a or a == float('inf') or a == -float('inf'):
            raise TypeError("a must be an integer")
    if isinstance(b, float):
        if b != b or b == float('inf') or b == -float('inf'):
            raise TypeError("b must be an integer")

#!/usr/bin/python3
"""
This module has one function: add_integer.
It safely adds two integers or floats, making sure they’re valid numbers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to int.

    Args:
        a: First number (int or float)
        b: Second number (int or float, default is 98)

    Returns:
        The sum of a and b as an integer

    Raises:
        TypeError: If either a or b is not an int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
