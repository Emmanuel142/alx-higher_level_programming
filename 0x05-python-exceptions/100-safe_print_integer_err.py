#!/usr/bin/python3
from sys import stderr
"""This module safely print integer
"""


def safe_print_integer_err(value):
    """This function print integer follow by a newline
    Args:
        value: accept all value but only print integers
    Returns:
        True: if the input is integer
        False: if the input is not integer
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print("Exception:",e, file=stderr)
        return False
