#!/usr/bin/python3
'''
This function returns the weighted average of all
integers tuple (<score>, <weight>)
'''


def weight_average(my_list=[]):

    if my_list:
        totalWeight = 0
        totalScoreWeight = 0

        for score, weight in my_list:
            totalScoreWeight += score * weight
            totalWeight += weight

        return totalScoreWeight / totalWeight
    else:
        return 0
