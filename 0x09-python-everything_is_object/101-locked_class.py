#!/usr/bin/python
'''
Module contains the class LockedClass
'''


class LockedClass:
    '''
    This is a class that only allows the creation of an
    attribute called first_name
    '''
    __slots__ = ('first_name', )
