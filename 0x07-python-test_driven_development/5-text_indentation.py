#!/usr/bin/python3

"""
This module defines a function that prints a text with 2
new lines after each of these characters ., ? and :
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these
    character ., ? and :

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a strig.
    """

    if text is None or not isinstance(text, str):
        raise TypeError("text must be a string")
    
    is_sp_ch = False

    for c in text:
        if is_sp_ch and (c == " " or c == "\t"):
            continue
        print(c, end="")
        is_sp_ch = False
        if c == "." or c == "?" or c == ":":
            is_sp_ch = True
            print("\n")
