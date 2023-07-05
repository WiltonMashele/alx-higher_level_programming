#!/usr/bin/python3
"""Defines a Rectangle class with width and height attributes"""


class Rectangle:
    """Representation of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return "Empty Rectangle"
        return "#" * self.__width + ("\n" + "#" * self.__width) * (self.__height - 1)

    def __repr__(self):
        """Return a string representation of the rectangle object"""
        return f"Rectangle(width={self.__width}, height={self.__height})"

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Deleting Rectangle object")

