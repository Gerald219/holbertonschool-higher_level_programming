#!/usr/bin/python3
"""
This module defines a function that prints a square with '#' characters.
"""


def print_square(size):
    """
    Prints a square with '#' characters of given size.

    Args:
        size: The size of the square sides (must be a non-negative integer).

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
