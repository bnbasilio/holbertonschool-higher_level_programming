#!/usr/bin/python3
"""Base class"""
from json import dumps, loads


class Base():
    """base of all classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON representation of list_objs to a file"""
        if not list_objs:
            objs = []
        else:
            objs = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w+") as f:
            f.write(cls.to_json_string(objs))
