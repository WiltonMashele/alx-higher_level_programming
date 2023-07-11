#!/usr/bin/python3
""" Module defining the Student class.
"""


class Student:
    """ Class to create instances of students."""

    def __init__(self, first_name, last_name, age):
        """ Initializes a student object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dictionary representation of the student."""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json_data):
        """ Replaces all attributes of the student instance."""
        for attr, value in json_data.items():
            setattr(self, attr, value)

