#!/usr/bin/python3
"""Defines a Rectangle class that from Base"""

from  models.base import Base


class Rectangle(Base):
    """Defines a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Create a new Rectangle object."""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """Get the height value of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height value of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """Get the x value of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x value of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("X value must be an integer")
        if value < 0:
            raise ValueError("X value must be non-negative")
        self.__x = value

    @property
    def y(self):
        """Get the y value of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y value of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Y value must be an integer")
        if value < 0:
            raise ValueError("Y value must be non-negative")
        self.__y = value

    def area(self):
        """Determine and return the area of the Rectangle."""
        return (self.__height * self.__width)

    def display(self):
        """Print the Rectangle using the #."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        for y in range(self.y):
            print()

        for x in range(self.__height):
            print(" " * self.x + "#" * self.__width)
