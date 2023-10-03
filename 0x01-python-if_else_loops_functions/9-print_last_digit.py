#!/usr/bin/python3

'''
This script contains a function that
prints the last digit and returns
the value as well
'''


def print_last_digit(number):
    strNum = str(number)
    lastDigit = strNum[-1]
    print(int(lastDigit), end='')

    return int(lastDigit)
