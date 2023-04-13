#!/usr/bin/python3
"""
This module defines a funtion that writes to a text file
returns the number of character written
"""


def write_file(filename="", text=""):
    """Writes as string to a text file (UTF8) and returns
    the number of character written.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
