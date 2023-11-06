#!/usr/bin/python3
'''
Contains the is_same_class function
'''


def is_same_class(obj, a_class):
    '''
    Returns True if obj is of specified class,
    otherwise returns False
    '''
    return type(obj) is a_class
