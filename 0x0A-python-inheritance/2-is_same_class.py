#!/usr/bin/python3
"""This module check if an object is a subclass of a class
"""


def is_same_class(obj, a_class):
    """This function check if object is
    an instance of a class
    """
    if issubclass(obj, a_class):
        return True
    return False
