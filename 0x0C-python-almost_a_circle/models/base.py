#!/usr/bin/python3
"""Base class"""
from json import dumps, loads
from os import path

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
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string or json_string is None:
            return []
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ is "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        list_instance = []
        if not path.exists(filename):
            return []
        with open(filename, 'r') as f:
            dictionary = cls.from_json_string(f.read())
        for key in dictionary:
            list_instance.append(cls.create(**key))
        return list_instance
