#!/usr/bin/python3
"""
This module defines a function that returns a python object
from a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Return the Python object representation of a JSON string.

    Args
        my_str (str): The Json string
    """
    return json.loads(my_str)
