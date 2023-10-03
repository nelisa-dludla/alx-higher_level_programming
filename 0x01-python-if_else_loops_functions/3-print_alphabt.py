#!/usr/bin/python3

'''
This script prints the alphabet
in lowercase, but excludes e and q
'''

for num in range(97, 123):
    if chr(num) == 'e' or chr(num) == 'q':
        pass
    else:
        print(chr(num), end="")
