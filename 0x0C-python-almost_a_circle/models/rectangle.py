#!/usr/bin/python3
"""This module declare a Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """This is a class of Rectangle
    Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        x (int): x
        y (int): y
    Attributes:
        height: get and set the height
        width: get and set the width
        x: get and set x
        y: get and set y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """get height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set height
        Raises:
            TypeError: if height is not int
            ValueError: if height is < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """get width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set width
        Raises:
            TypeError: if value is not int
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """get x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """set x
        Raises:
            TypeError: if x is not int
            ValueError: if x is < 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """set y
        Raises:
            TypeError: if y is not int
            ValueError: if y is < 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
