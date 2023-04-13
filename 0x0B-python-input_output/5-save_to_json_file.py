#!/usr/bin/python3
"""
This module define a function that saves a JSON representation
of an object ot a file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a JSON representation of an object to a file

    Args:
        my_obj (obj): The object.
        filename (str): The filename.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
