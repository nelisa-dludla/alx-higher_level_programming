#!/usr/bin/python3
'''
This function returns a set of common elements in
two sets
'''


def common_elements(set_1, set_2):
    mySet = set()

    for i in set_1:
        for j in set_2:
            if i == j:
                mySet.add(i)

    return mySet
