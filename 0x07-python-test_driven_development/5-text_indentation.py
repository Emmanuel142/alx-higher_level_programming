#!/usr/bin/python3
"""This module indent text
"""


def text_indentation(string):
    """This function indent by printing a newline
    when it enconter symbols like ", ? . :"
    Args:
        string (str): string of word
    Raise:
        
        TypeError: if the input is not string
    """
    if not isinstance(string, str):
        raise TypeError("text must be a string")
    symbols = [",", "?", ".", ":"]
    new_string = ""
    i = 0

    while i < len(string):
        new_string += string[i]
        if string[i] in symbols:
            new_string += "\n"
            i += 1
        if string[i] == " ":
            i += 1
            continue
        i += 1
    print(new_string, end="")
