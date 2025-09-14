#!/usr/bin/python3
"""This module is the base of all other classes in
    this project. It manage id in future classes and
    avoid duplicating code
"""
import json


class Base:
    """
    Attributes:
        nb_objects (int): private instance
        id (int): public instance
    if id is not None, id = id
    if id is None, id = nb_objects + 1
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method convert dictionaries to json
        Returns:
            str: Json string representation
        """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Save dictionary into Json file
            Args:
                cls (class): The class Square or Rect
                list_objs: item to save into json
        """
        with open(f"{cls.__name__}.json", "w") as file:
            content = to_json_string(list_objs)
            file.write(content)
