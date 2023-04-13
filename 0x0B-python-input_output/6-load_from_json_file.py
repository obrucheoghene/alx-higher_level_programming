#!/usr/bin/python3
"""
This module defines a function that create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the file.
    """
    with open(filename) as f:
        return json.load(f)
