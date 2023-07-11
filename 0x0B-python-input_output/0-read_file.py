#!/usr/bin/python3
"""This program reads a text file and prints its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and
    prints its contents to the standard output. Does not return any value.
    """

    try:
        with open(filename, "r", encoding="utf-8") as f:
            contents = f.read()
            print(contents, end="")
    except FileNotFoundError as e:
        print(f"File '{filename}' not found: {e}")
    except IOError as e:
        print(f"Error reading the file '{filename}': {e}")
