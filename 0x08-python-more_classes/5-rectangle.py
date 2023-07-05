#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Represents a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle with the given width and height."""
        self._width = width
        self._height = height

    @property
    def width(self):
        """Getter and setter for the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter and setter for the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join("#" * self._width for _ in range(self._height))

    def __repr__(self):
        """Returns a string representation of the rectangle object."""
        return "Rectangle({}, {})".format(self._width, self._height)

    def __del__(self):
        """Prints a message when the rectangle object is deleted."""
        print("Bye rectangle...")
