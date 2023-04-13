#!/usr/bin/python3
"""
This module defines a that returns the dictionary description
with simple data structure (list, dictionary, string, integer
and boolean) for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Return the dictionary represntation of a simple data structure.

    Args:
        obj (obj): An instance of a class
    """
    return obj.__dict__
