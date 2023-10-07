#!/usr/bin/python3
'''
Returns a tuple with the length of a string and
its first character
'''


def multiple_returns(sentence):

    strLength = len(sentence)

    if strLength:
        firstChar = sentence[0]
    else:
        firstChar = None

    returnTuple = (strLength, firstChar)

    return returnTuple
