#!/usr/bin/python3
"""Module defining the Student class and its methods."""

class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student instance with the provided attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the student instance.

        If `attrs` is provided, only include the specified attributes.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        valid_attrs = {}
        for attr in attrs:
            if isinstance(attr, str) and attr in self.__dict__:
                valid_attrs[attr] = self.__dict__[attr]
        return valid_attrs

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with the provided JSON.

        The JSON should be a dictionary containing the attribute-value pairs.
        """
        if isinstance(json, dict):
            self.__dict__ = json
