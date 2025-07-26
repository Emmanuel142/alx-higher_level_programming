#!/usr/bin/python3
"""This module defines a Student class
"""


class Student():
    """This class defines a student
    Args:
        first_name (str): The student first name
        last_name (str): The student last name
        age (int): The student age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This method return json of class
        """
        return self.__dict__
