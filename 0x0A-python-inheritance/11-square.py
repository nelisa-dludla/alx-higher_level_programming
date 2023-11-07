#!/usr/bin/python3
'''
Contains the class Square
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    A subclass that inherits from the class Rectangle
    '''
    def __init__(self, size):
        '''
        Initializes a new Square instance

        Args:
            size (int): The size of the square
        '''
        self.integer_validator('size', size)
        Rectangle.__init__(self, size, size)

        self.__size = size

    def area(self):
        '''
        Calculates the area of the sqaure

        Returns:
            int: The area of the square
        '''
        return self.__size ** 2

    def __str__(self):
        '''
        Returns the string representation of the square
        '''
        return '[Square] {}/{}'.format(self.__size, self.__size)
