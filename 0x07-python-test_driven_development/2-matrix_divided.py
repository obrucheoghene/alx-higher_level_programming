#!/usr/bin/python3

"""
This module defines a function matrix_divided, that
divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix

    Args:
        matrix (list): A list that represents a matrix
        div (int or float): The value of the divider

    Raises:
        TypeError: If the matrix is not a list of integers or floats.
        TypeError: If each row of the matrix is not of same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is equal to 0.
    Returns:
        (list): The new matrix after the division.
    """

    message = "matrix must be a matrix (list of lists) of integers/floats"
    row_len = None

    if not matrix or not isinstance(matrix, list):
        raise TypeError(message)

    for r in matrix:
        if not r or not isinstance(r, list):
            raise TypeError(message)

        for c in r:
            if not c or not isinstance(c, (int, float)):
                raise TypeError(message)

        if row_len is None:
            row_len = len(r)
        elif row_len != len(r):
            raise TypeError("Each row of the matrix must have the same size")

    if div is None or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(c / div, 2) for c in r] for r in matrix]
