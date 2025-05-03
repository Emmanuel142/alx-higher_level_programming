#!/usr/bin/python3

"""This module create a class of Square

    Todo:
        Create a Square class that initialize with size
        Check if the size is an integer and raise an error if it is not
        Check if the size is >= 0 and raise an error if not
"""


class Square:
    """This is a class of Squre with size

    Args:
        No arguments
    Attributes:
        No attributes
    """

    def __init__(self, size=0):
        """
        Args:
            size (int): The size of the square
        Raises:
            TypeError: if the input is not an integer
            ValueError: if the input is < 0
            """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
