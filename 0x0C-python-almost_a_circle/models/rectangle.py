#!/usr/bin/python3
"""
This module defines a rectangle class
"""
from models.base import Base


type_error_msg = "must be an integer"
size_value_error_msg = "must be > 0"
coordinate_value_error_msg = "must be >= 0"


class Rectangle(Base):
    """
    Represents the Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialise the Rectangle class

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
            x (int): The x coordinate of the Rectangle.
            y (int): The y coordinate of the Rectangle.
            id (int): The indentity of the Rectangle.

        Raises:
            TypeError: If width, height, x or y is not int.
            ValueError: If width or height is <= 0.
            ValueError: If x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the Rectangle width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the Rectangle width.
        """
        if type(value) is not int:
            raise TypeError("width " + type_error_msg)

        if value <= 0:
            raise ValueError("width " + size_value_error_msg)
        self.__width = value

    @property
    def height(self):
        """
        Getter for the Rectangle height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the Rectangle height.
        """
        if type(value) is not int:
            raise TypeError("height " + type_error_msg)

        if value <= 0:
            raise ValueError("height " + size_value_error_msg)
        self.__height = value

    @property
    def x(self):
        """
        Getter for the Rectangle x coordinate.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the Rectangle x coordinate.
        """
        if type(value) is not int:
            raise TypeError("x " + type_error_msg)

        if value < 0:
            raise ValueError("x " + coordinate_value_error_msg)
        self.__x = value

    @property
    def y(self):
        """
        Getter for the Rectangle y coordinate.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the Rectangle y coordinate.
        """
        if type(value) is not int:
            raise TypeError("y " + type_error_msg)

        if value < 0:
            raise ValueError("y " + coordinate_value_error_msg)
        self.__y = value

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        Prints Rectangle instance with #
        """
        [print() for y in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            for w in range(self.__width):
                print("#", end="")
            else:
                print()

    def update(self, *args, **kwargs):
        """
        Update teh rectangle class

        Args:
            *args (list): New attribute values
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.__width, self.__height, self.__x,
                                      self.__y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.__width, self.__height, self.__x,
                                      self.__y)
                    else:
                        self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v

    def to_dictionary(self):
        """
        Return the dictionary representation of Rectangle.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return string representation of rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)
