#!/usr/bin/python3
'''
This function deletes keys with a specific value
in a dictionary
'''


def complex_delete(a_dictionary, value):
    keysToDelete = []

    for key, keyValue in a_dictionary.items():
        if keyValue is value:
            keysToDelete.append(key)

    for key in keysToDelete:
        del a_dictionary[key]

    return a_dictionary
