#!/usr/bin/python3
'''
Contains the class BaseGeometry
'''


class BaseGeometry:
    '''
    Methods:
        area(self): Raises an Exception with the message
        area() is not implemented
    '''
    def __init__(self):
        pass

    def area(self):
        '''
        Raises an exception - area() is not implemented
        '''
        raise Exception('area() is not implemented')
