#!/usr/bin/python3
"""
This module defines a student class
"""


class Student:
    """
    Defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """Construct of the Student.
        Args:
            first_name (str): The student first name.
            last_name (str): The student last name.
            age (int): The student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return a dictionary representation of the Student.
        """
        return self.__dict__
