#!/usr/bin/python3

'''
This script contains a function that
checks for a lowercase character
'''


def islower(c):
    if ord(c) <= 122 and ord(c) >= 97:
        return True
    else:
        return False
