#!/usr/bin/python3
'''
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
'''

from requests import post
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        value = argv[1]
    else:
        value = ''

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': value}

    res_obj = post(url, data=data)

    try:
        json_data = res_obj.json()

        if json_data:
            print(f'[{json_data["id"]}] {json_data["name"]}')
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
