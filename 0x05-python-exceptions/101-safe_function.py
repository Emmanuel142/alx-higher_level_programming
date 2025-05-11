#!/usr/bin/python3
from sys import stderr

"""This module runs a function and pass it arguments
"""


def safe_function(fct, *args):
    """This function safely runs another function
    Args:
        fct (function): The function to run
        *args: the function parameters
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception:", e, file=stderr)
        return None
