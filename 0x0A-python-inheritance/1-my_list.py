#!/usr/bin/python3
"""The function defines an inherited list class MyList."""


class MyList(list):
    """Implements a sorted printing functionality for the built-in list class."""

    def print_sorted(self):
        """Prints the elements of the list in ascending order."""
        print(sorted(self))
