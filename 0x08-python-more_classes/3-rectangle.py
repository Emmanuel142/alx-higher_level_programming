#!/usr/bin/python3
"""This module defines a Rectangele
"""


class Rectangle():
    """This class defines a rectangle
    Args:
        No Arguments
    Attributes:
        height (int): The height of the rectangle
        width (int): The width of the rectangle
    Raise:
        TypeError: if input is not int
        """
    def __init__(self, height=0, width=0):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    def __str__(self):
        return '\n'.join('#' * self.height for _ in range(self.width))

    def __repr__(self):
        return '\n'.join('#' * self.height for _ in range(self.width))

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value=0):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value=0):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Area of a rectangle h * w
        """
        return self.height * self.width

    def perimeter(self):
        """The perimeter of a rectangle 2h + 2w
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)
