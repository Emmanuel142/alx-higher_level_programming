#!/usr/bin/python3
def remove_char_at(str, n):
    if len(str) < n:
        cpy = None
        for i in range(len(str)):
            if i == n:
                continue
            else:
                cpy[i] = str[i]
        print('{}'.format(cpy))
    else:
        print('{}'.format(str))
