#!/usr/bin/python3
"""Base Module"""


class Base:
    """This module defines a base class."""
    __nb_objects = 0

    def __init__(self, id=None):
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
