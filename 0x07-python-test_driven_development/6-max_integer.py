#!/usr/bin/python3
"""
Module to find the maximum integer in a list.
"""


def find_max_integer(lst=[]):
    """
    Finds and returns the maximum integer in a list of integers.

    If the list is empty, returns None.
    """
    if len(lst) == 0:
        return None
    max_num = lst[0]
    index = 1
    while index < len(lst):
        if lst[index] > max_num:
            max_num = lst[index]
        index += 1
    return max_num
