#!/usr/bin/python3
"""A module that defines a square class"""


class Square:
    """Square class task 1"""
    def __init__(self, size=0):
        """Initialize the square class"""
        self.size = size

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
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

    def __ne__(self, other):
        if isinstance(other, Square):
            return self.area() != other.area()
        return False

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False
