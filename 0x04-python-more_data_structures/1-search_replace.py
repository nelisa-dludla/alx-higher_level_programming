#!/usr/bin/python3
'''
This function replaces all occurrences of an element
by another in a new list
'''


def search_replace(my_list, search, replace):
    length = len(my_list)
    newList = []

    for i in range(length):
        if my_list[i] is search:
            newList.append(replace)
        else:
            newList.append(my_list[i])

    return newList
