#!/usr/bin/python3
"""4-append_write module"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file and returns
       the number of characters added"""
    with open(filename, "a+") as f:
        return f.write(text)
