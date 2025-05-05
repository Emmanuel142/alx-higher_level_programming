#!/usr/bin/python3

Square = __import__('6-square').Square

square = Square(3)
my_square = Square(5, (3, 5))
my_square.my_print()
square.my_print()
