#!/usr/bin/python3
"""1-my_list module"""


class MyList(list):
    """MyList inherits from list"""
    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
