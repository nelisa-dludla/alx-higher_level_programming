#!/usr/bin/python3
'''
This script takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
'''

from requests import get
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    res = get(url)

    var_value = res.headers.get('X-Request-Id')
    print(var_value)
