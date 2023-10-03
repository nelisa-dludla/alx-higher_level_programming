#!/usr/bin/python3

'''
This script contains a function that
prints the solution to the popular FizzBuzz question
'''


def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz', end=' ')
        elif i % 3 == 0:
            print('Fizz', end=' ')
        elif i % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(i, end=' ')
