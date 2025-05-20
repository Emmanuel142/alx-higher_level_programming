#!/usr/bin/python3
"""This module define a basegeometry with
    undefined area and validate integer
    """


class BaseGeometry():
    """The base geometry class
    """
    def area(self):
        """Return Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validate integer
            Args:
                name (str): The name of the geometry
                value (int): The integer value
            """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
