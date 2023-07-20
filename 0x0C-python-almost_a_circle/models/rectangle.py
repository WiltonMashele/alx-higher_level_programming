#!/usr/bin/python3
"""Defines a Rectangle class
that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Create a new Rectangle object."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width value of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width value of the rectangle."""
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """Get the height value of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height value of the rectangle."""
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
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

        for y in range(self.__y):
            print()

        for x in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns a formatted string representation of the Rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle.
        Arguments can be passed either as positional arguments (args) or 
        keyword arguments (kwargs).
        """
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0 and arg is not None:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id" and v is not None:
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}

