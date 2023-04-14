#!/usr/bin/python3
"""
This module defines a function that returns true True if the object is
exactly an instance of the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if object i exactly instance of a class

    Args:
        obj (object): The object to be checked
        a_class (a_class): The class to be compared with

    Return:
        (bool): True if instance, False otherwise
    """
    return isinstance(obj, a_class)
