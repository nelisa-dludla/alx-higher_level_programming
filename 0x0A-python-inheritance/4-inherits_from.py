#!/usr/bin/python3
'''
Contains the function inherits_from
'''


def inherits_from(obj, a_class):
    '''
    Returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class ;
    otherwise False.

    Args:
        obj (object): Object to be checked
        a_class (class) - Class to be checked against

    Returns:
        True if obj is an instance if an inherited class;
        Otherwise False
    '''
    return type(obj) is not a_class and issubclass(type(obj), a_class)
