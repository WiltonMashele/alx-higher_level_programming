#!/usr/bin/python3

"""a class Square that defines a square"""

class Square:
    def __init__(self, size):
        self.size = size

    def area(self):
        return self.size ** 2

    def perimeter(self):
        return 4 * self.size
