#!/usr/bin/python3

"""This modules create a Square
Todo:
    Create a class of Square
    Initialize the class with size with the optional value of zero
    Initialize the class with position(a tuple)
        with the optional value of (0,)
    Check for exception in input
    Calculate the area of the square
    Create a property retrieve the size
    Create a setter for the size attribute and check for error
    Create a property to retrieve the position
    Create a setter for the position attribute and check for error
    Create a method myprint that print the square with
        the '#'and empty line if the size is 0
    Position is filled with space when y > 0
    """


class Square:
    """A class of square

    Args:
        size (int): the size of the square
        position (tuple): the position of the square
    Attributes:
        No Attributes
    Raises:
        TypeError: if the input is not an integer or
            position is not a valid tuple
        ValueError: if the input is less than zero
        """
    def __init__(self, size=0, position=(0, 0)):
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """This returns the area of a square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """This property return the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This property set the value of the private attribute size
        Args:
        value (int): The size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """This property get the position of a square
        """
        return self.__position

    @position.setter
    def position(self, value=(0, 0)):
        """This property set the value position of a square
        Args:
            value (tuple):
            """
        if (not isinstance(position, tuple) or len(position) != 2
                or not all(isinstance(i, int) and i >= 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """This method print the square in the stdout with
        the '#' character and only newline if the area is zero
            Example:
                Square = __import__('5-square').Square
                my_square = Square(3)
                my_print()
                ----------------
                output
                ----------------
                ###
                ###
                ###
            """
        count = self.position[0]
        if self.size == 0:
            print()
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            while count > 0:
                print(" ", end="")
                count -= 1
            for j in range(self.size):
                print("#", end="")
            count = self.position[0]
            print()
        for i in range(self.position[1]):
            print()
