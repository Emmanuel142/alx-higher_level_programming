#!/usr/bin/python3
"""Square module
This modules define a square.
Todo:
    Create a class for a square.
"""


class Square:
    """Define a square with size.

    Attributes:
        __size (int): Private instance attribute.

    Methods:
        __init__(self, size=0): Initialize a Square instance
        with an optional size.
        area(self): Returns the area of a square
    """
    def __init__(self, size=0):
        """Initialize a Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate and return the area of a square

        Return:
            int: The area of a square
        """
        return self.__size**2
