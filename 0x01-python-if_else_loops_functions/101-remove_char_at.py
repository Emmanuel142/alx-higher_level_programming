#!/usr/bin/python3
def remove_char_at(str, n):
    if 0 <= n < len(str):
        cpy = list(str)
        del cpy[n]
        result = ''.join(cpy)
        return result
    else:
        return str
