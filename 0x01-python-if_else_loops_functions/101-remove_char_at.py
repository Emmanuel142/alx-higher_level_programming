#!/usr/bin/python3
def remove_char_at(str, n):
    if len(str) > n:
        cpy = list(str)
        del cpy[n]
        result = ''.join(cpy)
        print('{}'.format(result))
    elif str != None:
        print('{}'.format(s))
