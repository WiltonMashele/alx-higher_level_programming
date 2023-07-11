#!/usr/bin/python3


"""A class representing a rectangle that inherits from BaseGeometry."""
class BaseGeometry:
    def area(self):
        """Calculate the area of the geometry."""
        raise NotImplementedError("area() method not implemented.")

    def integer_validator(self, name, value):
        """Validate that the value is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be an integer greater than 0.")


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height
