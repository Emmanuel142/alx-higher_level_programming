#!/usr/bin/python3
from sys import argv, exit
if __name__ == "__main__":
    if len(argv) == 2:
        print('{:d} argument:\n{:d}: {}'.format(1, 1, argv[1]))
        exit()
    print('{:d} arguments:'.format(len(argv) - 1))
    for i in range(len(argv)):
        if i == 0:
            continue
        else:
            print('{:d}: {}'.format(i, argv[i]))
