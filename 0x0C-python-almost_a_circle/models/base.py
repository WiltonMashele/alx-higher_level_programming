#!/usr/bin/python3
"""Base Module"""

import json
from typing import List, Dict

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

class DataSerializer:
    """A utility class for data serialization."""
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

