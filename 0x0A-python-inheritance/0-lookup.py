#!usr/bin/python3
'''This module contains an implementation of the lookup method'''


def lookup(obj):
    '''Returns a list of available attributes and methods of an object'''
    return dir(obj)
