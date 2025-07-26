#!/usr/bin/python3
"""This module returns the dictionary description with
    simple data structure for json serialization of an object
"""
import json


def class_to_json(obj):
    """This function return the dictionart description with
    simple data structure of json serializzation of an object
    """
    return obj.__dict__
