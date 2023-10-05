#!/usr/bin/python3

'''
This program prints all the names defined by the compiled
module hidden_4.pyc
'''

import hidden_4


def main():
    functions = dir(hidden_4)

    for function in sorted(functions):
        if not function.startswith('__'):
            print(function)


if __name__ == '__main__':
    main()
