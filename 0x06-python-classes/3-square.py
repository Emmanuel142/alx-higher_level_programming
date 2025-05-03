#!/usr/bin/python3

"""This module create a Square class

Todo:
    Create a class of square
    Check if the input is in the right format and raise exception if not
    Calculate and return the area of the square
    """


class Square:
    """A class of Square

    Args:
        No argument
    Attributes:
        No attributes
    Raises:
        ValueError: if the input is less than 0
        TypeError: if the input is not integer
        """
    def __init__(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This method returns the area of the square
        which is size * size
        """
        return self.__size * self.__size
