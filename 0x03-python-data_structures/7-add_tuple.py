#!/usr/bin/python3
'''
Adds 2 tuples
'''


def add_tuple(tuple_a=(), tuple_b=()):
    listA = [0, 0]
    listB = [0, 0]

    if len(tuple_a) == 0:
        pass
    elif len(tuple_a) == 1:
        listA[0] = tuple_a[0]
    else:
        listA[0] = tuple_a[0]
        listA[1] = tuple_a[1]

    if len(tuple_b) == 0:
        pass
    elif len(tuple_b) == 1:
        listB[0] = tuple_b[0]
    else:
        listB[0] = tuple_b[0]
        listB[1] = tuple_b[1]


    value1 = listA[0] + listB[0]
    value2 = listA[1] + listB[1]

    newTuple = (value1, value2)

    return newTuple
