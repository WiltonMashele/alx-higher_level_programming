#!/usr/bin/python3
"""Base Module"""

import csv
import json
from typing import List, Dict
import turtle


class Base:
    """This module defines a base class."""
    __nb_objects = 0

    def __init__(self, id: int = None) -> None:
        """Constructor method that assigns the public instance attribute 'id'.

        Args:
            id (int): An integer value used to manage IDs in this project.

        Returns:
            None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries: List[Dict]) -> str:
        """Return the JSON serialization of a list of dictionaries.

        This method takes a list of dictionaries and returns its JSON representation.

        Args:
            list_dictionaries (list): A list of dictionaries to be serialized.

        Returns:
            str: JSON representation of the input list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Serialize a list of objects and save it to a JSON file.

        Args:
            list_objs (list): A list of objects derived from Base class.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                json.dump([], jsonfile)
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                json.dump(list_dicts, jsonfile)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string into a Python list.

        Args:
            json_string (str): The JSON string to be converted, representing a list of dictionaries.

        Returns:
            list: The Python list represented by the input JSON string. If the input string is None or empty,
                  an empty list is returned.
        """
        if json_string is None or json_string == "[]":
            return []
        
        try:
            return ast.literal_eval(json_string)
        except (ValueError, SyntaxError):
            return []

    @classmethod
    def create(cls, **attributes):
        """Return a class instantiated from a dictionary of attributes.

        Args:
            **attributes (dict): Key/value pairs of attributes to initialize the class.
        """
        instance = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        instance.update(**attributes)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Return a list of class instances created from a JSON file.

        Reads from a JSON file named '<ClassName>.json', where 'ClassName'
        is the name of the class in snake_case format.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes from the JSON data.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = json.load(jsonfile)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize a list of objects to a CSV file.

        Args:
            list_objs (list): A list of objects that inherit from the Base class.
            filename (str): The name of the file to write the CSV data to.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            if not list_objs:
                csvfile.write("[]")
            else:
                fieldnames = ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
    @classmethod
    def load_from_file_csv(cls):
        """Return a list of class objects instantiated from a CSV file.

        The function reads from '<cls.__name__>.csv' where 'cls' is the class name.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of class objects instantiated from the CSV file.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                next(reader)  # Skip the header row
                list_dicts = [dict([(k, int(v)) for k, v in d.items()]) for d in reader]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
