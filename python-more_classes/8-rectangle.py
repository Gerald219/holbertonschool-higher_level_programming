#!/usr/bin/python3
"""Rectangle class with customizable print symbol."""


class Rectangle:
    """Rectangle with width, height, count, and symbol."""

    # count and symbol for all rectangles
    number_of_instances = 0
    print_symbol = "#"

    # make a new rectangle
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # +1 each time made

    # width rules
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):  # must be number
            raise TypeError("width must be an integer")
        if value < 0:  # no negatives
            raise ValueError("width must be >= 0")
        self.__width = value

    # height rules
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):  # must be number
            raise TypeError("height must be an integer")
        if value < 0:  # no negatives
            raise ValueError("height must be >= 0")
        self.__height = value

    # area math
    def area(self):
        return self.__width * self.__height

    # perimeter math
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    # print rectangle with symbol
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.__width
                         for _ in range(self.__height))

    # recreate text
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    # delete rectangle
    def __del__(self):
        Rectangle.number_of_instances -= 1  # -1 when gone
        print("Bye rectangle...")

    # compare rectangles
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with bigger area, or rect_1 if equal."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
