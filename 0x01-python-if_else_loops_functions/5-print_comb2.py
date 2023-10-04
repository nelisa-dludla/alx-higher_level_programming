#!/usr/bin/python3

'''
This script prints numbers from
0 to 99
'''

for i in range(1, 100):

    if i == 99:
        print(i)
    else:
        print(i if i > 9 else '0{}'.format(i), end=', ')
