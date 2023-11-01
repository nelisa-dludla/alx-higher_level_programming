#!/usr/bin/python3
'''
This module includes one function, add_integer().
'''


def add_integer(a, b=98):
    '''
    Adds two integers

    Args:
        a (int/float): First integer
        b (int/float): Second integer

    Returns:
        int: The sum of the two integers

    Raises:
        TypeError: [a/b] must be an integer
    '''
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
