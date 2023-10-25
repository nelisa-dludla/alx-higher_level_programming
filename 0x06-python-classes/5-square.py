#!/usr/bin/python3
'''
This class defines a square.
'''


class Square:
    '''
    This class defines a square

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance.
        size(self): Getter method for the size attribute.
        size(self, value): Setter method for the size attribute.
        area(self): Calculates the area of the square.
        my_print(self): Prints the square to the console.
    '''

    def __init__(self, size=0):
        '''
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

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

    def area(self):
        '''
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        '''
        return pow(self.__size, 2)

    def my_print(self):
        '''
        Prints the square to the console.
        '''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
