#!/usr/bin/python3
'''
Finds all multiples of 2 in a list
'''


def divisible_by_2(my_list=[]):
    newList = []

    for element in my_list:
        if element % 2 == 0:
            newList.append(True)
        else:
            newList.append(False)

    return newList
