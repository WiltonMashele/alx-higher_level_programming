#!/usr/bin/python3
"""Defines a function to load Python objects from a JSON file."""

import json


def load_from_json_file(filename):
    """
    Load a JSON file and create a Python object.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename) as file:
        return json.load(file)
