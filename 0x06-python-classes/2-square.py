#!/usr/bin/python3
"""A module that defines a square class"""


class Square:
    """Square class task 1"""
    def __init__(self, size):
        """Initialize the square class"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
