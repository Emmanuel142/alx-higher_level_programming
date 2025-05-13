#!/usr/bin/python3

"""This module define a matrix of integers and divide them
"""


def matrix_divided(matrix, div):
    """This function divide items in matrix by the div
        Args:
            matrix (list): 2-dimensional matrix
            div (int): The value to divide matrix by
        Raise:
            TypeError: if div is not a number or list
                does is not integer or float
            """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[(round(i / div, 2)) for i in row] for row in matrix]
    return new_matrix
