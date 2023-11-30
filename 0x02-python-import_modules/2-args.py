#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    print('{:d} arguments:'.format(len(argv) - 1))
    for i in range(len(argv)):
        if i == 0:
            continue
        else:
            print('{:d}: {}'.format(i, argv[i]))
