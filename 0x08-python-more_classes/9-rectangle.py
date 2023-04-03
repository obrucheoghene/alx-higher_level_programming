#!/usr/bin/python3

"""
A module that defines a Rectangle class.
"""


class Rectangle:
    """
    A Rectangle class.

    Attributes:
        number_of_instances (int): Records the number of rectangle instances
        print_symbol (str): The symbol to be returned by the str method
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructor for Recatangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        Rectangle.number_of_instances += 1
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
            output = output + str(self.print_symbol) * (self.__width) + "\n"
        output = output + str(self.print_symbol) * (self.__width)
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
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Check if the rectangle is equal to the other rectangles.

        Args:
            rect_1 (Rectangle): The rectangle to be compared.
            rect_2 (Rectangle): The rectangle to be compared with.

        Returns:
            Rectangle: Returns the rectangle with the bigger area
            or rect_1 when both area equal
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Return a new rectangle instance

        Args:
            size (int): Represent the width and the height

        Returns:
            Rectangle: Returns a new rectangle.
        """
        if type(size) is not int:
            size = 0
        return Rectangle(size, size)
