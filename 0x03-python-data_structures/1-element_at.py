#!/usr/bin/python3
'''
Retrieves an element from a list like in C
'''


def element_at(my_list, idx):
    if not idx or idx > len(my_list) - 1:
        return None
    else:
        return my_list[idx]
