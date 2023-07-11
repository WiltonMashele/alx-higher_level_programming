#!/usr/bin/python3


"""A class representing a rectangle that inherits from BaseGeometry."""

class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle.

        :param width: The width of the new Rectangle.
        :type width: int
        :param height: The height of the new Rectangle.
        :type height: int
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
