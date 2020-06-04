#!/usr/bin/python3
"""100-append after module"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing a
       specific string"""
    if filename == "" or search_string == "" or new_string == "":
        return filename

    with open(filename) as f:
        _list = list(f)

    for i in range(len(_list)):
        if search_string in _list[i]:
            _list.insert(i + 1, new_string)

    with open(filename, 'w') as f:
        f.writelines(_list)

    return filename
