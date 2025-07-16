#!/usr/bin/python3
"""
"""
import sys, os


save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"

if os.path.exists(filename):
    my_list = load_from_json(filename)
else:
    my_list = []

if len(sys.argv) < 2:
    save_to_json(my_list, filename)
else:
    for i in range (len(sys.argv)):
        if i != 0:
            my_list.append(sys.argv[i])
    save_to_json(my_list, filename)
