#!/usr/bin/python3
"""
This module defines a function that append string to a file
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file and
    return the number of characters added.
    Args:
        filename (str): The name of the file.
        text (str): The string to append.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
