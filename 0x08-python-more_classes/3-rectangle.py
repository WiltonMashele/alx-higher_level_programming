#!/usr/bin/python3
"""Defines a Rectangle class that represents a rectangle.
"""


class Rectangle:
    """Class that represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self._width = width
        self._height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be >= 0.")
        self._width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be >= 0.")
        self._height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """Return a string representation of the rectangle using '#' characters."""
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join(["#" * self._width for _ in range(self._height)])
