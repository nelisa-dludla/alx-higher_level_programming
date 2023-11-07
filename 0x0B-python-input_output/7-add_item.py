#!/usr/bin/python3
'''
Adds all arguments to a Python list,
and then saves them to a file
'''

import sys
dumpJson = __import__('5-save_to_json_file').save_to_json_file
loadJson = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

try:
    pyData = loadJson('add_item.json')
except FileNotFoundError:
    pyData = []

pyData.extend(args)
dumpJson(pyData, 'add_item.json')
