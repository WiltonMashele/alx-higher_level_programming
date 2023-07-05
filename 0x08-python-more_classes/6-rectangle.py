#!/usr/bin/python3
"""This script defines a Rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle."""

    count = 0

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self._width = width
        self._height = height
        Rectangle.count += 1

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self._width

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self._height

    @width.setter
    def width(self, value):
        """Setter method for the width attribute."""
        if type(value) is not int:
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be non-negative.")
        self._width = value

    @height.setter
    def height(self, value):
        """Setter method for the height attribute."""
        if type(value) is not int:
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be non-negative.")
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
        """Returns a string representation of the rectangle using '#' characters."""
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join(["#" * self._width for _ in range(self._height)])

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return f"Rectangle(width={self._width}, height={self._height})"

    def __del__(self):
        """Prints a farewell message when an instance of Rectangle is deleted."""
        Rectangle.count -= 1
        print("Rectangle instance deleted.")

