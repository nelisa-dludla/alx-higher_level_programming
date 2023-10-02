#!/usr/bin/python3
'''
This script prints a string to stderr using the write function
from the sys module and exits with a status of 1
'''

import sys

sys.stderr.write('and that piece of art is useful - Dora Korpar, 2015-10-19\n')
sys.exit(1)
