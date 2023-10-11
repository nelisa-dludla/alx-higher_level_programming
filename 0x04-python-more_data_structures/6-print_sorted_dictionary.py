#!/usr/bin/python3
'''
This function prints a dictionary by ordered keys
'''


def print_sorted_dictionary(a_dictionary):
    sortedKeys = sorted(a_dictionary.keys())

    for key in sortedKeys:
        value = a_dictionary[key]
        print('{}: {}'.format(key, value))
