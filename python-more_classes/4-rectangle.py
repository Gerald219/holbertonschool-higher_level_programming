#!/usr/bin/python3
"""Rectangle class with width, height, area, perimeter, string and repr."""


class Rectangle:
    """Defines a rectangle that can give size info, print itself, and be recreated."""

    def __init__(self, width=0, height=0):
        self.width = width  # set width
        self.height = height  # set height

    @property
    def width(self):
        return self.__width  # get the current width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):  # must be a whole number
            raise TypeError("width must be an integer")
        if value < 0:  # must not be negative
            raise ValueError("width must be >= 0")
        self.__width = value  # store valid width

    @property
    def height(self):
        return self.__height  # get the current height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):  # must be a whole number
            raise TypeError("height must be an integer")
        if value < 0:  # must not be negative
            raise ValueError("height must be >= 0")
        self.__height = value  # store valid height

    def area(self):
        return self.__width * self.__height  # formula: width × height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0  # if flat, perimeter is 0
        return 2 * (self.__width + self.__height)  # formula: 2(w+h)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""  # return empty if no rectangle
        # build rows of "#" (width long), repeat for height
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        # return string that can recreate this rectangle
        return f"Rectangle({self.__width}, {self.__height})"
