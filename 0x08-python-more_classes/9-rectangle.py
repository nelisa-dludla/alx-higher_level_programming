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
        print_symbol (Any type): Symbol used for string representation

    Methods:
        __init__(self, width=0, height=0): Initializes a new rectangle instance
        area(self): Returns the area of the rectangle
        perimeter(self): Returns the perimeter of the rectangle
        bigger_or_equal(rect_1, rect_2): Returns the biggest rectangle
        square(cls, size=0): Returns a new Rectangle instance
        __str__(self): Returns the rectangle with the character #
        __repr__(self): Returns a string representation of the rectangle
        __del__(self): Prints a message when the instance is deleted
    '''
    number_of_instances = 0
    print_symbol = '#'

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        Returns the biggest rectangle based on area
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __repr__(self):
        '''
        Returns a string representation of the rectangle
        '''
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __str__(self):
        '''
        Returns the rectangle with the character #
        '''
        result = ''

        if self.__width == 0 or self.__height == 0:
            return result
        else:
            for row in range(self.__height):
                for _ in range(self.__width):
                    result += str(self.print_symbol)
                if row < self.__height - 1:
                    result += '\n'
            return result

    def __del__(self):
        '''
        Prints a message when instance is deleted
        '''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
