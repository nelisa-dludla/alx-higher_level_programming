#!/usr/bin/python3
'''
Function executes a function safely
'''

import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except (IndexError, ZeroDivisionError) as e:
        print('Exception: {}'.format(e), file=sys.stderr)
        return None
