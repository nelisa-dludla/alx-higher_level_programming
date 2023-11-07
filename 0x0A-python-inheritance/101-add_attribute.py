#!/usr/bin/python3
'''
Contains the function add_attribute
'''


def add_attribute(obj, name, value):
    '''
    Adds a new attribute to an object

    Args:
        obj (obj): The object attribute will be added to,
        if successful
        name (str): Name of the new attribute
        value (any): Value of the new attribute

    Raises:
        TypeError: If attribute can not be added
    '''
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
