#!/usr/bin/python3
"""This module declare a class Mylist that inherit
    from the class List
    """


class MyList(list):
    def print_sorted(self):
        return print(sorted(self))
