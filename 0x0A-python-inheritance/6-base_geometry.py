#!/usr/bin/python3
"""
Defines the BaseGeometry class, which represents a basic geometric shape.
"""


class BaseGeometry:
    """Represents the base geometry."""
    def area(self):
        """
        NotImplementedError: If the method is not overridden in a derived class.
        """
        raise NotImplementedError("area() method is not implemented")

