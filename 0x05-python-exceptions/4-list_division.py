#!/usr/bin/python3

"""This module divides divides a list of element by another
"""


def list_division(my_list_1, my_list_2, list_length):
    """This function takes list 1 and divide it with
    list 2
    Args:
        my_list_1 (list): first list (numerator)
        my_list_2 (list): second list (denomerator)
        list_length (int): The total length to be accessed
    Raises:
        IndexError: print "out of range"
        TypeError: print "wrong type"
        ZeroDivisionError: print "division by 0"
        """
    overall = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            overall.append(result)
    return overall
