#!/usr/bin/python3
'''
Contains the function save_to_json_file
'''

import json


def save_to_json_file(my_obj, filename):
    '''
    Writes an object to a text file,
    using a JSON representation
    '''
    jsonString = json.dumps(my_obj)

    with open(filename, 'w') as file:
        file.write(jsonString)
