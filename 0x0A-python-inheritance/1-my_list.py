#!/usr/bin/python3
'''
Contains the class MyList(list)
'''


class MyList(list):
    '''
    Subclass of list that provides a method to print the list in
    ascending sorted order.

    Attributes:
        Inherits all attributes and methods from the built-in list class.

    Methods:
        print_sorted - Prints a list in a ascending sorted order.
    '''

    def print_sorted(self):
        '''
        Prints a list in a ascending sorted order.

        Returns:
            None
        '''
        print(sorted(self))
