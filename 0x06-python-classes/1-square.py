#!/usr/bin/python3

"""a class Square that defines a square"""

class Square:
        """Represent a square."""

    def __init__(self, size):
        self.size = size

    def area(self):
        return self.size ** 2

    def perimeter(self):
        return self.size * 4
