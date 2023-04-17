#!/usr/bin/python3
"""
This module defines the "base" classe for all other classes
in this project.
"""


class Base:
    """
    Represents the Base class

    Args:
        __nb_objects (int): Number of base object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Base clase constructor

        Args:
            id (int, optional): The id attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
