#!/usr/bin/python3
"""This module import from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This inherit from Rectangle
        Args:
            size (int): size of the square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """This method determine the area size^2
        """
        return self.__size * self.__size
    
    def __str__(self):
        return "[Square] {}/{}".format(self.__width, self.__height)
