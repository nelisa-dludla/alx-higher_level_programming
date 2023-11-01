#!/usr/bin/python3
'''
Module contains one function, print_square().
'''


def print_square(size):
    '''
    Args:
        size (int): The size of the square to be printed

    Raises:
        TypeError:
            If size is not an integer
            If size is a float and less than zero

        ValueError:
            If size is less than zero
    '''

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    for _ in range(size):
        for _ in range(size):
            print('#', end='')
        print()
