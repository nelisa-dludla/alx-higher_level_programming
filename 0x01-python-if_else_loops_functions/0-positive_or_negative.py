#!/usr/bin/python3

'''
This script prints a random number
and tells you if it is postive,
negative or zero
'''

import random
number = random.randint(-10, 10)

if number < 0:
    print(f'{number} is negative')
elif number > 0:
    print(f'{number} is positive')
else:
    print(f'{number} is zero')
