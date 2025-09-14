#!/usr/bin/python3

"""This module define a function that check if object
    is instance of a class
"""


def inherits_from(obj, a_class):
    """This function return True if the object is instance of a
    class that inherit a class
    """
    if isinstance(obj, a_class):
        return True
    return False
