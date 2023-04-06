#!/usr/bin/python3

"""
This module provides a function to add two integers
"""


def add_integer(a, b=98):
    """
    Return the sum of two integers

    Args:
        a (int or float): The first value.
        b (int or float, optional): The second value.

    Raises:
        TypeError: If a and b are not integers or floats.

    Returns
        int: The sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
