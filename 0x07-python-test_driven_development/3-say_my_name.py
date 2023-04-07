#!/usr/bin/python3

"""
This module defines say_my_name function that prints my name
"""


def say_my_name(first_name, last_name=""):
    """
    This modules prints my name is <first name> <last name>

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Raises:
        TypeError: If the first_name or last_name is not a string.
    """

    if not first_name or not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
