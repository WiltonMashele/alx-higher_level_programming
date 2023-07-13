#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
from typing import Union
from rectangle import Rectangle


class Square(Rectangle):
"""Represent a square."""

    def __init__(self, side_length: Union[int, float]):
    """Initialize a new square.

    Args:
        side_length (Union[int, float]): The length of each side of the square.
    """
    self.integer_validator("side_length", side_length)
    super().__init__(side_length, side_length)
    self.__side_length = side_length
