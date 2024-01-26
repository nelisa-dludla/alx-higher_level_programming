#!/usr/bin/python3
'''
This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8)
'''

from urllib import request, parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    data = {'email': argv[2]}
    encoded_data = parse.urlencode(data).encode('utf-8')

    req_obj = request.Request(url, data=encoded_data, method='POST')

    with request.urlopen(req_obj) as res:
        content = res.read().decode('utf-8')
        print(content)
