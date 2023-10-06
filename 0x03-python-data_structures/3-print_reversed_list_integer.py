#!/usr/bin/python3
'''
Prints all integers of a list, in reverse order
'''


def print_reversed_list_integer(my_list=[]):
    length = (len(my_list) * -1) - 1

    for i in range(-1, length, -1):
        print('{:d}'.format(my_list[i]))
