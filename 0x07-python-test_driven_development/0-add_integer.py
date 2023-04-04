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
    
    Returns
        int: The sum of a and b
    """
    if type(a) is not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) is not in [int, float]:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
