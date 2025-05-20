#!/usr/bin/python3
"""This module import from basegeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherit from BaseGeometry
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of rectangle 2h + 2w
        """
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
