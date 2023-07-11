#!/usr/bin/python3
"""Defines a function for appending text to a file."""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters appended.
    """
    character_count = 0
    with open(filename, "a", encoding="utf-8") as file:
        for char in text:
            file.write(char)
            character_count += 1
    return character_count
