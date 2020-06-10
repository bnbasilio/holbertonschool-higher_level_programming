#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """a rectangle has width, height, x, y and id"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def validate(self, name, value):
        """validates input"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if name in ["width", "height"] and value <= 0:
            raise ValueError('{} must be > 0'.format(name))
        if name in ['x', 'y'] and value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x"""
        self.validate('x', value)
        self.__x = value

    @property
    def y(self):
        """gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y"""
        self.validate('y', value)
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints the Rectangle instance with the character #"""
        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print(' ' * self.__x + "#" * self.__width)

    def __str__(self):
        """returns string representation of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.__width, "height":
                self.__height, "x": self.__x, "y": self. __y}
