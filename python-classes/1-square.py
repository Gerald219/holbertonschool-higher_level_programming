#!/usr/bin/python3
"""Module that creates a Square with a hidden size value."""


class Square:
    """Square class with a private size attribute, if accessed gives error."""

    def __init__(self, size):
        """Initialize the square with a given size (not validated yet)."""
        self.__size = size
