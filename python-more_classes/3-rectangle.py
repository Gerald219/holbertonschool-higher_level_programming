#!/usr/bin/python3
"""Rectangle class with width, height, area, perimeter, string"""


class Rectangle:
    """A rectangle with width, height, area, perimeter, and print form."""

    def __init__(self, width=0, height=0):
        self.width = width  # set width, runs setter check
        self.height = height  # set height, runs setter check

    @property
    def width(self):
        return self.__width  # stored width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):  # check type → must be int
            raise TypeError("width must be an integer")
        if value < 0:  # check value - no negatives
            raise ValueError("width must be >= 0")
        self.__width = value  # save width

    @property
    def height(self):
        return self.__height  # get stored height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):  # check type, must be int
            raise TypeError("height must be an integer")
        if value < 0:  # check value, no negatives
            raise ValueError("height must be >= 0")
        self.__height = value  # save height

    def area(self):
        return self.__width * self.__height  # calc area - w × h

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0  # if flat - no perimeter
        return 2 * (self.__width + self.__height)  # calc, sum up

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""  # if flat → empty string
        return "\n".join("#" * self.__width for _ in range(self.__height))
        # build rows of # - width times, repeat for height
