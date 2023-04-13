#!/usr/bin/python3
"""
This module defines a function to insert a string
when a search string is found in a line.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert new_string after a line containing the search string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
