#!/usr/bin/python3
"""This module return an object of json
"""
import json


def from_json_string(my_str):
    """This function return the object(Python data structure)
    represented by a Json string
    """
    return json.loads(my_str)
