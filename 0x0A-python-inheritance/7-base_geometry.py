#!/usr/bin/python3
'''
Contains the class BaseGeometry
'''


class BaseGeometry:
    '''
    Methods:
        area(self): Raises an Exception with the message
        area() is not implemented

        integer_validator(self, name, value): Validates value
    '''
    def __init__(self):
        pass

    def area(self):
        '''
        Raises an exception - area() is not implemented
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        Validates value

        Args:
            name (str): A string
            value (int): An integer

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        '''
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
