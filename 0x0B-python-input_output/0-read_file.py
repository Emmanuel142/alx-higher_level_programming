#!/usr/bin/python3
"""This module read a text file
"""


def read_file(filename=""):
    """This function read a text file (UTF)
    and print it to the stduot
    """
    with open (filename, "r") as f:
        file = f.read()
        print(file)
