#!/usr/bin/python3
"""13-student module"""


class Student:
    """a student has a first and last name and age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            _dict = {}
            if type(attrs) == list:
                for attr in attrs:
                    if type(attr) == str and attr in self.__dict__:
                        _dict[attr] = self.__dict__[attr]
            return _dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for attr in json:
            self.__dict__[attr] = json[attr]
