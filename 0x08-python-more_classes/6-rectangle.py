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
        number_of_instances (int): The number of Rectangle instances

    Methods:
        __init__(self, width=0, height=0): Initializes a new rectangle instance
        area(self): Returns the area of the rectangle
        perimeter(self): Returns the perimeter of the rectangle
        __str__(self): Returns the rectangle with the character #
        __repr__(self): Returns a string representation of the rectangle
        __del__(self): Prints a message when the instance is deleted
    '''
    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        '''
        Calculates the area of the rectangle

        Returns:
            int: The area of the rectangle
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''
        Calculates the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __repr__(self):
        '''
        Returns a string representation of the rectangle
        '''
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __str__(self):
        '''
        Returns the rectangle with the character #
        '''
        str = ''

        if self.__width == 0 or self.__height == 0:
            return str
        else:
            for row in range(self.__height):
                for _ in range(self.__width):
                    str += '#'
                if row < self.__height - 1:
                    str += '\n'
            return str

    def __del__(self):
        '''
        Prints a message when instance is deleted
        '''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
