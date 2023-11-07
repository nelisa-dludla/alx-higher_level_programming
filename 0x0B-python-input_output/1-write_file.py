#!/usr/bin/python3
'''
Contains the function write_file
'''


def write_file(filename="", text=""):
    '''
    Writes a string to a text file

    Args:
        filename: Name of a file
        text: String to be written to the file

    Returns:
        int: Numbers of characters written
    '''
    with open(filename, 'w') as file:
        numOfCharacters = len(text)
        file.write(text)

    return numOfCharacters
