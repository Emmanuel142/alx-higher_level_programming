#!/usr/bin/python3
"""This module define a function that print
    square with #
    """


def print_square(size):
    """This function print square with a #
    Args:
        size (int): size of the square
    Raise:
        TypeError: if size is not int
        """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
