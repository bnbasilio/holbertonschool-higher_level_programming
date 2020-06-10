#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """a square has a size, x, y, and id"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """gets the size(width or height)"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size(width and height)"""
        self.validate("width", value)
        self.width = value
        self.height = value
