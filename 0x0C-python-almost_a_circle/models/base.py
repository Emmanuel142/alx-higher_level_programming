#!/usr/bin/python3
"""This module is the base of all other classes in
    this project. It manage id in future classes and
    avoid duplicating code
"""


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
        if id is not None:
            self.id = id
        __nb_objects = __nb_objects + 1
        self.id = __nb_objects
