#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a > b and b > c:
        return a * b - c
    elif c > a and c > b:
        return c
    else:
        return a + b
