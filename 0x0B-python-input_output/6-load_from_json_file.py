#!/bin/usr/python3

"""This module create and object from json file
"""
import json


def loads_from_json_file(filename):
    """This function loads from json file
    and save into file 'filename'
    """
    with open(filename, encoding="utf-8") as f:
        j_file = json.load(filename)
        f.read(jfile)
