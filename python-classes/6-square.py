#!/usr/bin/python3

"""This module defines a Square class that manages size, position, and
printing.

Size and position are validated.
The class can compute area and print the square at the given position.
"""


class Square:
    """Square with size, position, area, and printing behavior."""

    def __init__(self, size=0, position=(0, 0)):
        """Set up square with size and position."""
        # start square with size + position
        # send value to setter for checks
        self.size = size
        # check and save position (uses setter)
        self.position = position

    @property
    def size(self):
        """Return size value."""
        # give back hidden size
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with rules."""
        # must be an int
        if not isinstance(value, int):
            # error if not
            raise TypeError("size must be an integer")
        # must not be negative
        if value < 0:
            # error if negative
            raise ValueError("size must be >= 0")
        # save hidden size
        self.__size = value

    @property
    def position(self):
        """Return position value."""
        # give back hidden position
        return self.__position

    @position.setter
    def position(self, value):
        """Set position with rules."""
        # check all rules
        # must be a tuple
        # must have 2 items
        # both must be int
        # both must be >= 0
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        # save hidden position
        self.__position = value

    def area(self):
        """Return area (size * size)."""
        # size times size
        return self.__size * self.__size

    def my_print(self):
        """Print square with # shifted by position."""
        # if size is 0: print empty line
        if self.__size == 0:
            print("")
            return
        # move down by position[1]
        for _ in range(self.__position[1]):
            print("")
        # each row: spaces then #'s
        for _ in range(self.__size):
            # add spaces for x offset, then print #
            print(" " * self.__position[0] + "#" * self.__size)
