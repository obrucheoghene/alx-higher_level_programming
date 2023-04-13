#!/usr/bin/python3
"""
This module defines a student class which includes
a function to filter student attribute
"""


class Student:
    """
    Defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """Contructor of Student class.
        Args:
            first_name (str): The student first name.
            last_name (str): The student last name.
            age (int): The student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a filtered dictionary representation of the Student.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(key) == str for key in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
