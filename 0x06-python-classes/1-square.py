#!/usr/bin/python3

"""Square
This module create a class square with size
Todo:
    Create a class of square that initialize with size
"""


class Square:
    """This is a class of square that instatinize with size

    Args:
        No argument
    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size):
        """ Initialize a squaure with size

        Args:
            size (int): The size of the square
        """
        self.__size = size
