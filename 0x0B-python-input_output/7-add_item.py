#!/usr/bin/python3
"""This module take arguments and save it in a
    json file
    Module:
        save_to_json_file (fnc) = takes input and save to
                                a specified json file
        load_from_json_file = load a json file for use
"""
import sys
import os


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
    for i in range(len(sys.argv)):
        if i != 0:
            my_list.append(sys.argv[i])
    save_to_json(my_list, filename)

