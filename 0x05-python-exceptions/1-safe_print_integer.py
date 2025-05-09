#!/usr/bin/python3

"""This module print an integer
"""

def safe_print_integer(value):
    """This function print integer
        Args:
            value: Can be any type
        """
    try:
        if isinstance(value, int):
            print(value)
            return True
        else:
            return False
    except Exception(e):
        print(e)
