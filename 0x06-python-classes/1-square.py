#!/usr/bin/python3
"""Square module
This modules define a square.
Todo:
    Create a class for a square.
"""


class Square:
    """Define a square with size.

    Attributes:
        size: Private instance attribute.

    Methods:
        No methods.
    """
    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): Private instance attribute.
        """
        self.__size = size
