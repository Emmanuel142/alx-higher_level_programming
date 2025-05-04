#!/usr/bin/python3

Square = __import__('6-square').Square

my_square = Square(5, ("a", 5))
print(my_square.size)
print(my_square.area())
my_square.my_print()
