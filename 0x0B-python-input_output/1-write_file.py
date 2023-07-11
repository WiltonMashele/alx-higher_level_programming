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
    char_count = 0
    with open(filename, "r+", encoding="utf-8") as f:
        f.seek(0, 2)
        start_position = f.tell()
        for char in text:
            f.write(char)
            char_count += 1
        end_position = f.tell()
        appended_chars = end_position - start_position

    return appended_chars
