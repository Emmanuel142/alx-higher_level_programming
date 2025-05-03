#!/usr/bin/python3

"""This modules create a Square
Todo:
    Create a class of Square
    Initialize the class with size with the optional value of zero
    Check for exception in input
    Calculate the area of the square
    Create a property retrieve the size
    Create a setter for the size attribute
    """


class Square:
    """A class of square

    Args:
        No arguments
    Attributes:
        No Attributes
    Raises:
        TypeError: if the input is not an integer
        ValueError: if the input is less than zero
        """
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """This returns the area of a square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """This property return the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This property set the value of the private attribute size
        Args:
        value (int): The size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
