#!/usr/bin/python3
'''
Contains the class Square
'''

from .rectangle import Rectangle

class Square(Rectangle):
    '''
    A child class that inherits from the Rectangle class

    Attributes:
        size (int): The size of the square
        x (int): The x value of the square
        y (int): The y value of the square
        id (int): The id of the instance

    Methods:
        __init__(self, size, x=0, y=0, id=None): Initializes a new Square instance
        size(self): Getter method for size
        size(self, value): Setter method for size
        update(self, *args, **kwargs): Assigns an argument to each attribute
        to_dictionary(self): Returns the dictionary representation of Square
        __str__(self): Returns the string representation of Square
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initializes a new Square instance
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
        Getter method for size

        Returns:
            int: The size of Square
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        Setter method for size

        Args:
            value (int): The new size of Square
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        Assigns an argument to each attribute
        '''
        if args:
            self.id = args[0]

            if len(args) > 1:
                self.width = args[1]

            if len(args) > 2:
                self.x = args[2]

            if len(args) > 3:
                self.y = args[3]
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        '''
        Returns a dictionary representation of a Square
        '''
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}

    def __str__(self):
        '''
        Returns the string representation of Square
        '''
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'
