#!/usr/bin/python3

Square = __import__('4-square').Square

S = Square(5)
try:
    print (S.area())
    print(S.size)

    S.size = 7

    print(S.area())
    S.size = "8"
    print(S.size)
    print(S.area())
except Exception as e:
    print(e)
