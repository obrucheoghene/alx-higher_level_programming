#!/usr/bin/python3
"""
This module defines a function that returns true True if the object inherits
from a specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Check if object inherits from a specified class

    Args:
        obj (object): The object to be checked
        a_class (a_class): The super class

    Return:
        (bool): True if inherited, False otherwise
    """
    return issubclass(obj, a_class)
