#!/usr/bin/python3
"""
This module defines a function to read a file
"""


def read_file(filename=""):
    """
    Reads and print a text file in stdout

    Args:
        filename (str): The Filename.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
