#!/usr/bin/python3
'''
This function converts a Roman numeral to an integer
'''


def roman_to_int(roman_string):
    romanNums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

    currentValue = 0
    nextValue = 0
    sum = 0

    if roman_string and type(roman_string) is str:
        for i in range(len(roman_string)):
            currentValue = romanNums[roman_string[i]]

            if i + 1 < len(roman_string):
                nextValue = romanNums[roman_string[i + 1]]
            else:
                nextValue = 0

            if currentValue < nextValue:
                sum -= currentValue
            else:
                sum += currentValue

        return sum
    else:
        return 0
