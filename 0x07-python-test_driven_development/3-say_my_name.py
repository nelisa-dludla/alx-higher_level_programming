#!/usr/bin/python3
'''
This module includes one function, say_my_name().
'''


def say_my_name(first_name, last_name=""):
    '''
    Prints string: My name is <first name> <last name>.

    Args:
        first_name (str): First name
        last_name (str): Last name

    Returns:
        str: The formatted string including first and last name

    Raises:
        TypeError:
            If first name is not a string
            If last name is not a string
    '''

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
