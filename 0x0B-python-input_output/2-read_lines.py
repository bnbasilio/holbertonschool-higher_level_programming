#!/usr/bin/python3
"""2-read_lines module"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file and prints it to stdout"""
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for line in f:
                print(line, end="")
                nb_lines -= 1
                if nb_lines <= 0:
                    return
