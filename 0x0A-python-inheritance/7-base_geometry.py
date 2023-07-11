#!/usr/bin/python3

"""
This script defines the BaseGeometry class, which represents a base geometry.
"""


class BaseGeometry:
    """Represents a base geometry."""
    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        raise NotImplementedError("area() method is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
