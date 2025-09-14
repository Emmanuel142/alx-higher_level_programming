#!/usr/bin/python3

"""This module print the x element of a list
"""


def safe_print_list(my_list=[], x=0):
    """This function print item in a list
        Args:
            my_list (list)= This is the list of all types(int,str,...)
            x (int) = The number of item to be printed
        """
    try:
        store = ""
        count = 0
        for item in my_list:
            if x != count:
                store += str(item)
                count += 1
        print(store)
        return count
    except Exception as e:
        print(e)
