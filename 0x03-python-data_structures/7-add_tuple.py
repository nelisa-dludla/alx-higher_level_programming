#!/usr/bin/python3
'''
Adds 2 tuples
'''


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        newTupleA = (tuple_a[0], 0)
    elif len(tuple_b) < 2:
        newTupleB = (tuple_b[0], 0)
    else:
        firstIndeValue = tupddle_a[0] + tuple_b[0]
        secondIndexValue = tuple_b[0] + tuple_b[0]
