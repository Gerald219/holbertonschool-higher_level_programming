#!/usr/bin/python3
"""Rectangle class with width and height validation."""


class Rectangle:
    """Defines a rectangle by width and height."""

    def __init__(self, width=0, height=0):
        self.width = width  # set width (uses setter)
        self.height = height  # set height (uses setter)

    @property
    def width(self):
        return self.__width  # return width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):  # must be int
            raise TypeError("width must be an integer")
        if value < 0:  # must be >= 0
            raise ValueError("width must be >= 0")
        self.__width = value  # save value

    @property
    def height(self):
        return self.__height  # return height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):  # must be int
            raise TypeError("height must be an integer")
        if value < 0:  # must be more or equal - >= 0
            raise ValueError("height must be >= 0")
        self.__height = value  # save value
