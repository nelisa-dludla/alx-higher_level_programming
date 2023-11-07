#!/usr/bin/python3
'''
Contains the function load_from_json_file
'''

import json


def load_from_json_file(filename):
    '''
    Creates an Object from a JSON file

    Args:
        filename (JSON): The filename
    '''
    with open(filename, 'r') as file:
        content = file.read()
        pythonObj = json.loads(content)

        return pythonObj
