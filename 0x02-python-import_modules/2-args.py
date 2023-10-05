#!/usr/bin/python3

'''
This script prints the number of and list of
its arguments
'''

import sys


def main():
    arguments = sys.argv
    length = len(arguments) - 1

    if length == 0:
        print('0 arguments.')
    elif length == 1:
        print('{} argument:'.format(length))
    else:
        print('{} arguments:'.format(length))

    for i in range(1, length + 1):
        print('{}: {}'.format(i, arguments[i]))


if __name__ == '__main__':
    main()
