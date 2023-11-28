#!/usr/bin/python3
def remove_char_at(s, n):
    if len(s) > n:
        cpy = list(s)
        del cpy[n]
        result = ''.join(cpy)
        print('{}'.format(result))
    else:
        print('{}'.format(s))
