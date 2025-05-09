#!/usr/bin/python3
"""This module print integers in a list
"""


def safe_print_list_integers(my_list=[], x=0):
    """This function print list of integer
        Args:
            my_list[] (list): List of items(int, str,...)
            x (int): The depth of item to print
        """
    try:
        item_count = 0
        printed_count = 0
        score = ""
        for item in my_list:
            if isinstance(item, int):
                score += str(item)
                printed_count += 1
            else:
                pass
            if item_count != x:
                item_count += 1
            else:
                raise Exception('x is bigger than the list')
        print("{:d}".format(int(score)))
    except Exception as e:
        print(e)
