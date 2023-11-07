#!/usr/bin/python3
'''
Contains the class MyInt
'''


class MyInt(int):
    '''
    A subclass that inherits from the class int

    Attributes:
        Inherits all attribute from the int class

    Methods:
        __eq__(self, obj): Inverts the equality operator
        __ne__(self, obj): Inverts the inequality operator
    '''
    def __eq__(self, obj):
        '''
        Inverts the equality operator

        Args:
            obj: An object to compare with

        Returns:
            bool: The inverted comparison result
        '''
        return not super().__eq__(obj)

    def __ne__(self, obj):
        '''
        Inverts the inequality operator

        Args:
            obj: An object to compare with

        Returns:
            bool: The inverted comparison result

        '''
        return not super().__ne__(obj)
