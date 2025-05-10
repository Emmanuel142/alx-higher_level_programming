#!/usr/bin/python3

"""This module divides divides a list of element by another
"""


def list_division(my_list_1, my_list_2, list_length):
    """This function takes list 1 and divide it with
    list 2
    Args:
        my_list_1 (list): Takes any input(int,str,etc)
        my_list_2 (list): Takes any input(int,str,etc)
        list_lenght (int): The total length to be accessed
    Raises:
        IndexError: print "out of range"
        TypeError: print "wrong type"
        ZeroDivisionError: print "division by 0"
        """
    result = None
    overall = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            overall.append(result)
        except TypeError:
            print("wrong type")
            overall.append(0)
        except IndexError:
            print("out of range")
            return overall
        except ZeroDivisionError:
            print("division by 0")
            overall.append(0)
        finally:
            print(overall)
    return overall
