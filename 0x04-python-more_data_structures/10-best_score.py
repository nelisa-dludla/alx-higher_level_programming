#!/usr/bin/python3
'''
This function returns a key with the biggest
integer value
'''


def best_score(a_dictionary):
    maxValue = 0
    maxValueKey = ''

    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > maxValue:
                maxValue = value
                maxValueKey = key
        return maxValueKey
    else:
        return None
