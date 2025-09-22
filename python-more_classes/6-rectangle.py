#!/usr/bin/python3
"""Rectangle class with instance counter."""


class Rectangle:
    """Rectangle counts how many exist."""

    number_of_instances = 0  # counter - counts rectangles

    def __init__(self, width=0, height=0):
        self.width = width  # set width
        self.height = height  # set height
        Rectangle.number_of_instances += 1  # add +1 when created

    @property
    def width(self):
        return self.__width  # get width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):  # must be int = number
            raise TypeError("width must be an integer")
        if value < 0:  # no negatives
            raise ValueError("width must be >= 0")
        self.__width = value  # save width

    @property
    def height(self):
        return self.__height  # get height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):  # must be int = number
            raise TypeError("height must be an integer")
        if value < 0:  # no negatives allowed
            raise ValueError("height must be >= 0")
        self.__height = value  # save the height

    def area(self):
        return self.__width * self.__height  # width × height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0  # no perimeter if flat
        return 2 * (self.__width + self.__height)  # 2(w+h) multiply by 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))
        # draw rectangle

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"  # recreate

    def __del__(self):
        Rectangle.number_of_instances -= 1  # reduces by 1
        print("Bye rectangle...")  # show message when deleted
