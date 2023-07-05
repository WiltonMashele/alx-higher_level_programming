#!/usr/bin/python3
"""Defines a Rectangle class with width and height attributes"""


class Rectangle:
    """Representation of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object with optional width and height"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """Getter method for the width attribute"""
        return self._width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute"""
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter method for the height attribute"""
        return self._height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute"""
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self._height = value

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        return 2 * (self._width + self._height)

    def __str__(self):
        """Return a string representation of the rectangle"""
        return f"Rectangle (width={self._width}, height={self._height})"

    def __repr__(self):
        """Return a string representation of the rectangle object"""
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Deleting Rectangle object")

