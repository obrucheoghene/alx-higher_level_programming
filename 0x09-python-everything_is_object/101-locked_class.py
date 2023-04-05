#!/usr/bin/python3

"""
This module defines a class LockedClass
"""


class LockedClass:
    """
    The class prevents the user for dynamically creating new instances
    attributes, except if the new instance attribute is called firstname

    Attributes:
        first_name (str): The first name
    """

    __slots__ = ['first_name']

    def __init__(self):
        """
        Constructor of LockedClass
        """
        self.first_name = "first_name"
