#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with the given width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self._width = self._validate_input(width)
        self._height = self._validate_input(height)

    def _validate_input(self, value):
        """
        Validates that the given value is a positive integer.

        Args:
            value: The value to be validated.

        Returns:
            int: The validated value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        if value < 0:
            raise ValueError("Value must be >= 0")
        return value

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle to the given value.

        Args:
            value (int): The new width value.
        """
        self._width = self._validate_input(value)

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle to the given value.

        Args:
            value (int): The new height value.
        """
        self._height = self._validate_input(value)

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)
