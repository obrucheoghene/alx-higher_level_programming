#!/usr/bin/python3
"""A module that defines a square class"""


class Square:
    """Square class task 1"""
    def __init__(self, size=0):
        """Initialize the square class"""
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Size getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter method"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
