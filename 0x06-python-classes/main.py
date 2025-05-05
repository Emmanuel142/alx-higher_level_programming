#!/usr/bin/python3

Square = __import__('6-square').Square

square = Square(3)
my_square = Square(5, (3, 5))
print(square.size)
print(square.area())
square.my_print()
