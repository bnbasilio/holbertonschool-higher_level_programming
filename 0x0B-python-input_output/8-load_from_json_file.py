#!/usr/bin/python3
"""8-load_from_json_file module"""
import json


def load_from_json_file(filename):
    """creates an object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
