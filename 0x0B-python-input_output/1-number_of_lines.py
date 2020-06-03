#!/usr/bin/python3
"""1-number_of_lines module"""

def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    lines = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
        return lines
