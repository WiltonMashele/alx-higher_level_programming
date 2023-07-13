#!/usr/bin/python3
"""The function defines an inherited list class MyList."""


class MyList(list):
    """Implements a sorted printing functionality for the built-in list class."""

    def print_sorted(self):
        """Prints the elements of the list in ascending order."""
        sorted_list = [x for x in sorted(self)]
        print(sorted_list)

