#!/usr/bin/python3
"""This module declare a class Mylist that inherit
    from the class List
    """


class MyList(list):
    """This class print sort list
    """
    def print_sorted(self):
        """This is the method to print sorted list
        """
        return print(sorted(self))
