#!/usr/bin/python3
'''
This script takes in a URL, sends a request to the URL
and displays the body of the response
'''

from requests import get, exceptions
from sys import argv

if __name__ == '__main__':
    url = argv[1]

    try:
        res = get(url)
        res.raise_for_status()
        print(res.text)
    except exceptions.HTTPError as err:
        err_code = err.response.status_code
        print(f'Error code: {err_code}')
