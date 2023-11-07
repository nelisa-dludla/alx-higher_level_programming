#!/usr/bin/python3
'''
Contains the function to_json_string
'''

import json


def to_json_string(my_obj):
    '''
    Returns the JSON representation of an object

    Args:
        my_obj (obj): An object

    Returns:
        str: The JSON representation of the object
    '''
    jsonString = json.dumps(my_obj)
    return jsonString
