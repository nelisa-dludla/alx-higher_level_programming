#!/usr/bin/python3
'''
Contains the function read_file
'''


def read_file(filename=""):
    '''
    Reads a text file and prints it to stdout

    Args:
        filename: The name of the file to be read
    '''
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')
