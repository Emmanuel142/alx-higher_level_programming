#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) > 96 and ord(c) < 124:
            c = ord(c) - 26
        else:
            c = c
