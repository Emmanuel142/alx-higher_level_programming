#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if c >= 'a' and c <= 'z':
            c = ord(c) - 32
        else:
            c = c
    print('{}'.format(str)
