#!/usr/bin/python3
'''
This script takes in a URL and an email address, sends a POST request
o the passed URL with the email as a parameter, and finally displays
the body of the response
'''

from requests import post
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    data = {'email': argv[2]}

    req_obj = post(url, data=data)
    print(req_obj.text)
