#!/usr/bin/python3
'''
This module contains one function, text_indentation()
'''


def text_indentation(text):
    '''
    Args:
        text (str): Text to be processed

    Raises:
        TypeError: If text is not a string
    '''

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    punctuation = ['.', '?', ':']
    lastChar = ''

    for currentChar in text:
        if lastChar in punctuation and currentChar == ' ':
            pass
        else:
            print(currentChar, end='')

        if currentChar in punctuation:
            print('\n')

        lastChar = currentChar
