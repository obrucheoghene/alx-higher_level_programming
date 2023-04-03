#!/usr/bin/python3

"""
A module that defines a Rectangle class.
"""


class Rectangle:
    """
    A Rectangle class.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Constructor for Recatangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calcuate and return the area of the retangle.

        Returns:
            int: The area of the reactangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calcuate and return the perimeter of the retangle.

        Returns:
            int: The perimeter of the reactangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string represention of the rectangle to end users

        Returns:
            str: The area of the rectantle in #
        """
        output = ''

        if self.__width == 0 or self.__height == 0:
            return output

        for i in range(self.__height - 1):
            output = output + "#" * (self.__width) + "\n"
        output = output + "#" * (self.__width)
        return output

    def __repr__(self):
        """
        Return a string representation of the rectangle that can be
        used with eval() to recreate the rectangle.

        Returns:
            str: A string representation of the rectangle that can be used with
            eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Delete the rectangle instance
        """
        print("Bye rectangle...")
