#!/usr/bin/python3

"""This module create a class of Square
"""


class Square:
    """This class 
    """


    def __init__(self, size):
        """
        """
        if type(size) != int:
            raise TypeError:
                print("size must be an integer")
        if size < 0:
            raise ValueError:
                print("size must be >= 0")

        self.__size = size
