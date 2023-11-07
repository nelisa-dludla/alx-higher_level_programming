#!/usr/bin/python3
'''
Contains the function class_to_json
'''


def class_to_json(obj):
    '''
    Returns the dictionary description with simple data for
    JSON serialization of an object

    Args:
        obj: Object

    Returns:
        Dictionary description of the object
    '''
    return obj.__dict__
