#!/usr/bin/python3
"""Defines a square with a getter and setter"""


class Square:
    """a square"""

    def __init__(self, size=0):
        """initializes square"""
        self.__size = size

    def size(self):
        """gets the size of square"""
        return self.__size

    def size(self, value):
        """sets the size of square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates the area of the square"""
        return (self.__size ** 2)
