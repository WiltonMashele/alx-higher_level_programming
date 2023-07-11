#!/usr/bin/python3
"""Defines a function for inserting text into a text file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a specified string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within each line of the file.
        new_string (str): The string to insert after each line.
    """
    text = ""
    with open(filename, "r") as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as file:
        file.write(text)
