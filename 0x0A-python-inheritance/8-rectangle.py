#!/usr/bin/python3
"""
Defines a retangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a retangle class that inherits form BaseGeometry
    """

    def __init__(self, width, height):
        """
        Constructor of a new Rectangle.
        Args:
            width (int): The width.
            height (int): The height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
