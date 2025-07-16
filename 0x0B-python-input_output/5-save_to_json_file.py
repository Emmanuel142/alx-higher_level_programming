#!/usr/bin/python3
"""This module save file to json
"""
import json



def save_to_json_file(my_obj, filename):
    """This function save object to json representation
    into text file
    Args:
        my_obj (str): object to save to json
        filename (str): name of the text file
        """
    with open(filename, "w") as f:
        jrep = json.dumps(my_obj)
        return f.write(jrep)
