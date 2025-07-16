#!/usr/bin/python3
"""This module create and object from json file
"""
import json


def load_from_json_file(filename):
    """This function loads from json file 'filename'
    and return the corresponding Object
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
