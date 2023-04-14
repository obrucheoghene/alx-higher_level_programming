#!/usr/bin/python3
"""
This module defines a function that returns thee list of availagle
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (object): The object.

    Return:
        (list): The list of available attributes and method.
    """

    return dir(obj)
