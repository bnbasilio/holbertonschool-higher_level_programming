#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    argv = argv[1:]
    argc = len(argv)
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[0])
        b = int(argv[2])
        if argv[1] not in '+-*/':
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if argv[1] == '+':
                result = add(a, b)
            elif argv[1] == '-':
                result = sub(a, b)
            elif argv[1] == "*":
                result = mul(a, b)
            elif argv[1] == '/':
                result = div(a, b)
            print("{:d} {} {:d} = {:d}".format(a, argv[1], b, result))
