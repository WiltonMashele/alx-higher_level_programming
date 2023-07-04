#!/usr/bin/python3
"""
Defines an empty class Rectangle
"""


class Rectangle:
    """
    Representation of a rectangle.

    Attributes:
    - width: The width of the rectangle.
    - height: The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with width and height.

        Args:
        - width: The width of the rectangle. Defaults to 0.
        - height: The height of the rectangle. Defaults to 0.
        """
        self.__height = 0
        self.__width = 0
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the private instance attribute width.

        Args:
        - value: The width value to set.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be greater than or equal to 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the private instance attribute height.

        Args:
        - value: The height value to set.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be greater than or equal to 0")
        self.__height = value
