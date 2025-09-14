#!/usr/bin/python3
"""This module define a basegeometry with
    undefined area
    """


class BaseGeometry():
    """The base geometry class
    """
    def area(self):
        """Return Exception
        """
        raise Exception("area() is not implemented")
