#!/usr/bin/python3
'''
Handles basic calculator operations like addition,
substraction, multiplication and division
'''

from calculator_1 import add, sub, mul, div
import sys


def main():
    argv = sys.argv
    length = len(argv)
    operators = ['+', '-', '*', '/']

    if length < 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]

        if op == operators[0]:
            res = add(a, b)
            print('{:d} {:s} {:d} = {:d}'.format(a, op, b, res))
        elif op == operators[1]:
            res = sub(a, b)
            print('{:d} {:s} {:d} = {:d}'.format(a, op, b, res))
        elif op == operators[2]:
            res = mul(a, b)
            print('{:d} {:s} {:d} = {:d}'.format(a, op, b, res))
        elif op == operators[3]:
            res = div(a, b)
            print('{:d} {:s} {:d} = {:d}'.format(a, op, b, res))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)


if __name__ == '__main__':
    main()
