#!/usr/bin/python3
"""This module define a function that check if object
    is instance of a class
"""


def inherits_from(obj, a_class):
    """This function return True if the object is instance of a
    class that inherit from a class
    """
    print(isinstance(obj, a_class) or issubclass(obj, class))
