#!/usr/bin/python3

"""This module create a class of Square
"""


class Square:
    """This is a class of Squre with size

    Args:
        NO arguments
    Attributes:
        NO attributes

    """


    def __init__(self, size):
        """
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
