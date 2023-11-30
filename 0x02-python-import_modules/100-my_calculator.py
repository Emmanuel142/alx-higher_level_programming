#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = argv[2]
    operators = ["+", "-", "*", "/"]
    if oprator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(arg[1])
    b = int(arg[3])
    if operator == "+":
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    elif operator == "-":
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
    elif oprator == "/":
        print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
    else:
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
    exit(0)
