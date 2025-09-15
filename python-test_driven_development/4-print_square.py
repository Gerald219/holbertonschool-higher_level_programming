#!/usr/bin/python3
"""
This module provides a function to print a square using the `#` character.
It validates the input size to ensure correctness and raises exceptions
when invalid types or values are passed.
"""


def print_square(size):
    """
    Print a square made of `#` characters of size x size.

    Args:
        size (int): The length of each side of the square. Must be >= 0.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Prints:
        A square pattern of '#' characters with dimensions size by size.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
