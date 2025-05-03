#!/usr/bin/python3

Square = __import__('4-square').Square

S = Square(5)

print (S.area())
print(S.size)

S.size = 7

print(S.area())
