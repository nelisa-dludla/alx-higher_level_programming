#!/usr/bin/python3
'''
This function adds all unique integers in a list
(only once for each integer)
'''


def uniq_add(my_list=[]):
    uniqSet = set()
    uniqSum = 0

    for i in my_list:
        uniqSet.add(i)

    for j in uniqSet:
        uniqSum += j

    return uniqSum
