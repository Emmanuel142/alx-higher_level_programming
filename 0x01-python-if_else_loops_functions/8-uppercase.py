#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if c >= 'a' and c <= 'z':
            c = ord(c) - 26
            print('{}'.format(chr(c)), end="")
        else:
            print('{}'.format(chr(c), end="")
