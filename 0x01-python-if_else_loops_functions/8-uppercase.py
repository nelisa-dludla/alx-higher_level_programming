#!/usr/bin/python3

'''
This script contains a function that
prints a string in uppercase
'''


def uppercase(str):
    newStr = ''

    for c in str:
        if ord(c) >= 65 and ord(c) <= 90:
            newStr += c
        elif ord(c) >= 97 and ord(c) <= 122:
            charUpper = chr(ord(c) - 32)
            newStr += charUpper
        else:
            newStr += c

    print(newStr)
