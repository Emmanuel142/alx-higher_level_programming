#!/usr/bin/python3
"""This module defines a class of Square.
    It inherits from Rectangle module
    and defines a square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a square
    Attributes:
        size (int): the size of the square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """This init inherit from the Rectangle
        Args:
            size (int): size of the square
            x (int): x coordinate
            y (int): y coodinate
            id (int): inherit id from Base
        """
        super().__init__(width, height, x, y, id)

    def __str__(self):
        """The string representation
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """This attribute returns the size
        of the Square
        """
        return self.width

    @size.setter
    def size(self, value):
        """This set the size of the square
        Args:
            value (int): The size of the square
        """
        self.width = value
        self.height = value
