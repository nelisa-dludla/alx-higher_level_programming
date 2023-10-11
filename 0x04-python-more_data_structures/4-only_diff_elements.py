#!/usr/bin/python3
'''
This function returns a set of all elements present
in only one set
'''


def only_diff_elements(set_1, set_2):
    mySet = set()
    commonEle = set()

    for i in set_1:
        if i in set_2:
            commonEle.add(i)
        else:
            mySet.add(i)

    for j in set_2:
        if j not in commonEle:
            mySet.add(j)

    return mySet
