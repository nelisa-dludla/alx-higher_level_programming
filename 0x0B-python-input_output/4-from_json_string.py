#!/usr/bin/python3
'''
Contains the function from_json_string
'''

import json


def from_json_string(my_str):
    '''
    Returns an object (Python data structure) from
    a JSON string

    Args:
        my_str: A JSON string

    Returns:
        obj: A python object (Data structure)
    '''
    pythonObj = json.loads(my_str)
    return pythonObj
