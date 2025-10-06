#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """width and height validated by BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Rectangle after validating inputs"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return string format like [Rectangle] width/height"""
        return f"[Rectangle] {self.__width}/{self.__height}"
