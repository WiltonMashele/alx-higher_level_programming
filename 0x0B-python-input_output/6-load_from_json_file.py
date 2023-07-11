#!/usr/bin/python3
""" Module that loads an object from a JSON file
"""
import json


def load_object_from_json_file(filename):
    """ Function that loads an object from a JSON file

    Args:
        filename: Name of the JSON file

    Returns:
        The loaded object

    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
