#!/usr/bin/python3
"""
Define the class MyList that is a subclass of the built-in list class.
"""


class MyList(list):
    """
    Subclass of list that provides additional functionality.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
