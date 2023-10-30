#!/usr/bin/python3
'''
Module contains the class Rectangle
'''


class Rectangle:
    '''
    Class defines a rectangle

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle

    Methods:
        __init__(self, width=0, height=0): Initializes a new rectangle instance
    '''
    def __init__(self, width=0, height=0):
        '''
        Initializes a new rectangle instance

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        Raises:
            TypeError:
                If width is not an integer
                If height is not an integer

            ValueError:
                If width is less than 0
                If height is less than 0
        '''
        if not isinstance(width, int):
            raise TypeError('width must be an integer')

        if width < 0:
            raise ValueError('width must be >= 0')

        if not isinstance(height, int):
            raise TypeError('height must be an integer')

        if height < 0:
            raise ValueError('height must be >= 0')

        self.__height = height
        self.__width = width

    @property
    def width(self):
        '''
        Getter method for the width attribute

        Returns:
            int: The width of the rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter method for the width attribute

        Args:
            value (int): The new width of the rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        '''
        Getter method for the height attrbute

        Returns:
            int: The height of the rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter method for the height attribute

        Args:
            value (int): The new height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
