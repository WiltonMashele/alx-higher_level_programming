#!/usr/bin/python3

"""
This module defines a class Rectangle that inherits from BaseGeometry.
"""

from typing import Union
from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry.
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Initializes a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self) -> int:
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self) -> str:
        """
        Returns the string representation of a Rectangle.
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
