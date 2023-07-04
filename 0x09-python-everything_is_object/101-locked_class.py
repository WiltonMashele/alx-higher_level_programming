#!/usr/bin/python3
"""
Defines a locked class that restricts attribute creation to 'first_name'.
"""


class LockedClass:
    """
    This class prevents the user from creating new attributes
    except for 'first_name'.
    """

    __slots__ = ("first_name",)
