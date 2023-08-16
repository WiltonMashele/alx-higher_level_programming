#!/usr/bin/python3
"""
Square module that inherits from
the base class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Getter for the size property
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Setter for the size property
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square
        """
        dict_res = super().to_dictionary()
        dict_res["size"] = dict_res.pop("width")
        return dict_res
