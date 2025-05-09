#!/usr/bin/python3
"""This module print integers in a list
"""


def safe_print_list_integers(my_list=[], x=0):
    """This function print list of integer
        Args:
            my_list[] (list): List of items(int, str,...)
            x (int): The depth of item to print
        """
    printed_count = 0
    score = ""
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_count += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            break
    print()
    return printed_count
