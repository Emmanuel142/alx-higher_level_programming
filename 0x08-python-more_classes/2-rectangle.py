#!/usr/bin/python3
"""Rectangle class

"""


class Rectangle:
    """Define a class Rectangle

    Attributes:
        width (int): Width of the rectangle
        height (int): Height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialize a rectangle

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of a Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of a Rectangle

        Args:
            value (int): The value of the width
        Raises:
            ValueError: if the value is less than 0
            TypeError: if the value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

        @property
        def height(self):
            """The Height of the Rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            """Get the height of the rectangle

            Args:
                value (int): the value of the height
            Raises:
                TypeError: if the value is not an interger
                ValueError: if the value is less than 0
            """
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Returns the area of the rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Returns the perimeter of the rectanle."""
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)
