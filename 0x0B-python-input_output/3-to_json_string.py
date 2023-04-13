#!/usr/bin/python3
"""
This module defines a function that returns a JSON
representation of and object.
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of a string object.

    Args:
        my_obj (obj): The object.
    """
    return json.dumps(my_obj)
