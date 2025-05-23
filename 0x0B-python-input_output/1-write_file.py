#!/usr/bin/python3
"""This module write to file
"""


def write_file(filename="", text=""):
    """This function write to file
        Args:
            filename (str)= The output string (output.txt)
            text (str)= The text writing to file
        """
    with open(filename, "w") as f:
        f.write(text)
