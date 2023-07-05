#!/usr/bin/python3

"""
This class defines a rectangle.
It represents an empty rectangle initially, with no width or height specified.
"""

class Rectangle:
    """
    This class defines a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with optional width and height.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Getter method for the width of the rectangle.
        """
        return self._width

    @property
    def height(self):
        """
        Getter method for the height of the rectangle.
        """
        return self._height

    @width.setter
    def width(self, value):
        """
        Setter method for the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be >= 0.")
        self._width = value

    @height.setter
    def height(self, value):
        """
        Setter method for the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be >= 0.")
        self._height = value

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)
