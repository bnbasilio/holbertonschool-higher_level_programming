#!/usr/bin/python3
"""2-is_same_class module"""


def is_same_class(obj, a_class):
    """checks if the object is exactly an instance of the class"""
    return type(obj) is a_class
