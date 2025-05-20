#!/usr/bin/python3
"""This module define ...
"""


def inherits_from(obj, a_class):
    """This function return True if the object is instance of a
    class that inherit from a class
    """
    print(isinstance(obj, a_class) or issubclass(obj, class))
