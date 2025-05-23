#!/usr/bin/python3
"""This module append file
"""


def append_write(filename="", text=""):
    """This function append string to the
    end of a file and create a new file if
    if the file does not exist
    Args:
        filename (str)= The string of output(.txt)
        text (str) = The string to append
    """
    with open(filename, "a") as f:
        f.write(text)
