#!/usr/bin/python3
"""This module define a function that return True
    if obj is an instance of a class
    """


def is_kind_of_class(obj, a_class):
    """This function return true if object is an instance
    of a class or is a subclass of a class else false
    """
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    return False
