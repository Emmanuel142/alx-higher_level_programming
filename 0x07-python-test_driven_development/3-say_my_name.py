#!/usr/bin/python3
"""This module define a function that print
    My name is <first name> <last name>
    """


def say_my_name(first_name, last_name=""):
    """This module print first name and last name
    Args:
        first_name (str): first string of name
        last_name (str): second string of name
    Raise:
        TypeError: if the input is not string
        """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
