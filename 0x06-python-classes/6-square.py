#!/usr/bin/python3
'''
This class defines a square.
'''


class Square:
    '''
    This class defines a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position on the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a new Square.
        size(self): Getter method for the size attribute.
        size(self, value): Setter method for the size attribute.
        position(self): Getter method for the position attribute.
        position(self, value): Setter method for the position attribute.
        area(self): Calculate the area of the square.
        my_print(self): Prints the square to the console.
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: If size is not an integer or if position
            is not a tuple of 2 positive integers

            ValueError: If size is less than 0
        '''

        typeErrMsg = 'position must be a tuple of 2 positive integers'

        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError(typeErrMsg)

        for coord in position:
            if not isinstance(coord, int) and coord > 0:
                raise TypeError(typeErrMsg)

        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Setter method for the size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        '''
        Getter method for the position attribute.

        Returns:
            tuple: The position of the square.
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        Setter method for the position attribute.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        '''

        typeErrMsg = 'position must be a tuple of 2 positive integers'

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(typeErrMsg)

        for coord in value:
            if not isinstance(coord, int) and coord > 0:
                raise TypeError(typeErrMsg)

        self.__position = value

    def area(self):
        '''
        Calculates the area of the square.

        Returns:
            int: The are of the sqaure.
        '''
        return pow(self.__size, 2)

    def my_print(self):
        '''
        Prints the square to the console.
        '''
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
