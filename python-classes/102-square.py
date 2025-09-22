#!/usr/bin/python3
"""Square that can compare itself by area."""


class Square:
    """Square with size, area, and comparisons."""

    def __init__(self, size=0):
        """Start square with size (default 0)."""
        self.size = size  # validate through setter

    @property
    def size(self):
        """Get size."""
        return self.__size  # return stored size

    @size.setter
    def size(self, value):
        """Set size (must be int or float >= 0)."""
        if not isinstance(value, (int, float)):   # type check
            raise TypeError("size must be a number")
        if value < 0:                             # range check
            raise ValueError("size must be >= 0")
        self.__size = value                       # store valid size

    def area(self):
        """Get area (size * size)."""
        return self.__size * self.__size

    # compare squares by area
    def __eq__(self, other):  # ==
        # equal: True if both areas are the same
        return self.area() == other.area()

    def __ne__(self, other):  # !=
        # not equal: True if areas are different
        return self.area() != other.area()

    def __lt__(self, other):  # <
        # less than: True if this area is smaller
        return self.area() < other.area()

    def __le__(self, other):  # <=
        # less or equal: True if smaller or exactly equal
        return self.area() <= other.area()

    def __gt__(self, other):  # >
        # greater than: True if this area is bigger
        return self.area() > other.area()

    def __ge__(self, other):  # >=
        # greater or equal: True if bigger or exactly equal
        return self.area() >= other.area()
