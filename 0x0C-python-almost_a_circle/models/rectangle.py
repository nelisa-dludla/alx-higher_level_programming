#!/usr/bin/python3
'''
Contains the class Rectangle
'''

from .base import Base
import json

class Rectangle(Base):
    '''
    A child class that inherits from the Base class

    Attributes:
        width (int): Width of the Rectangle
        height (int): Height of the Rectangle
        x (int): x position
        y (int): y position

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a new Rectangle instance
        width(self): Getter method for width
        width(self, value): Setter method for width
        height(self): Getter method for height
        height(self, value): Setter method fot height
        x(self): Getter method for x
        x(self, value): Setter method for x
        y(self): Getter method for y
        y(self, value): Setter method for y
        area(self): Calculates the area of Rectangle
        display(self): Prints Rectangle to stdout
        update(self, *args): Assigns an argument to each attribute
        to_dictionary(self): Returns the dictionary representation of Rectangle
        __str__(self): Returns the string representation of Rectangle
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initializes a new Rectangle instance

        Args:
            width (int): Width of the Rectangle
            height (int): Height of the Rectangle
            x (int): x position
            y (int): y position
        '''

        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')

        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')

        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''
        Getter method for width

        Returns:
            int: The width of Rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter method for width

        Args:
            value (int): The new width of Rectangle
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):
        '''
        Getter method for height

        Returns:
            int: The height of Rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter method for height

        Args:
            value (int): The new height of Rectangle
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        '''
        Getter method for x

        Returns:
            int: The x value of Rectangle
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Setter method for x

        Args:
            value (int): The new value of x
        '''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        '''
        Getter method for y
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Setter method for y
        '''
        self.__y = value

    def area(self):
        '''
        Calculates the area of Rectangle

        Returns:
            int: The area of Rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''
        Prints Rectangle to stdout
        '''

        for _ in range(self.__y):
                print()

        for _ in range(self.__height):
            for _ in range(self.__x):
                print(' ', end='')

            for _ in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        '''
        Assigns an argument to each attribute
        '''

        if args:
            self.id = args[0]

            if len(args) > 1:
                self.width = args[1]

            if len(args) > 2:
                self.height = args[2]

            if len(args) > 3:
                self.x = args[3]

            if len(args) > 4:
                self.y = args[4]
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])
    def to_dictionary(self):
        '''
        Returns the dictionary representation of Rectangle
        '''
        return {"x": self.__x, "y": self.__y, "id": self.id, "height": self.__height, "width": self.__width}

    def __str__(self):
        '''
        Returns the string representation of Rectangle
        '''
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}'
