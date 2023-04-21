#!/usr/bin/python3
"""
This module defines the "base" classe for all other classes
in this project.
"""
import json
import os
import csv
import turtle


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
            json_string (str): The string representation a list of
            dictionaries
        Returns:
            (list) : If json_string is None or empty, return an empty list
            Otherwise, return the list represented by json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        Args:
            dictionary (dic): Instance attributes
        Return:
            Instance with all attributes set.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                dummy = cls(1)
            else:
                dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a json file
        """
        filename = cls.__name__ + ".json"

        if os.path.isfile(filename) is False:
            return []
        with open(filename, "r") as jsonfile:
            list_obj = Base.from_json_string(jsonfile.read())
            return [cls.create(**obj) for obj in list_obj]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write CSV Serialization of list of objects to a file

        Args:
            list_objs (list): List of objects
        """
        filename = cls.__name__ + "csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write('[]')
            else:
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                else:
                    fieldnames = ["id", "width", "height", "x", "y"]
                csvfile_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    csvfile_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize a list of objects from a CSV file

        Return:
            (list): List of instance of object
        """
        filename = cls.__name__ + ".csv"

        if os.path.isfile(filename) is False:
            return []
        with open(filename, "r", newline="") as csvfile:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
            list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
            return [cls.create(**d) for d in list_dicts]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """

        for rect in list_rectangles:
            turtle.showturtle()
            turtle.up()
            turtle.goto(rect.x, rect.y)
            turtle.down()
            for i in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)
            turtle.hideturtle()

        turtle.color("#b5e3d8")
        for sq in list_squares:
            turtle.showturtle()
            turtle.up()
            turtle.goto(sq.x, sq.y)
            turtle.down()
            for i in range(2):
                turtle.forward(sq.width)
                turtle.left(90)
                turtle.forward(sq.height)
                turtle.left(90)
            turtle.hideturtle()

        turtle.exitonclick()
