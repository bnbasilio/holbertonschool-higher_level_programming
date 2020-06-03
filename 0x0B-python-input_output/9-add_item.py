#!/usr/bin/python3
"""9-add_item module"""
import os.path
import sys
save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

_list = []
if os.path.exists("add_item.json"):
    _list = load("add_item.json")

for i in range(1, len(sys.argv)):
    _list.append(sys.argv[i])

save(_list, "add_item.json")
