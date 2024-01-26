#!/usr/bin/python3
'''
This script fetches https://alx-intranet.hbtn.io/status
'''

from requests import get

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    res = get(url)

    print('Body response:')
    print(f'\t- type: {type(res.text)}')
    print(f'\t- content: {res.text}')
