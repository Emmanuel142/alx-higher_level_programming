#!/usr/bin/python3

"""This module add two integers
"""


def add_integer(a, b=98):
    """This function add two integer
    Param:
        a (int,float): The first element
        b (int,float): The second element
    Return:
        TypeError: if a or b is not a float or int
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
