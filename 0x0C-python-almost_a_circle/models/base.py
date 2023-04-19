#!/usr/bin/python3
"""
This module defines the "base" classe for all other classes
in this project.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of JSON string representation

        Args:
            json_string (string): The string representation a list of
            dictionaries
        """
        if json_string is None or json_string == "[]":
            return []
        return json.load(json_string)
