#!/usr/bin/python3

'''
This script prints the ASCII alphabet, in reverse order,
alternating between lowercase and uppercase
'''

for c in range(122, 96, -1):
    print('{}'.format(chr(c)), end='')
