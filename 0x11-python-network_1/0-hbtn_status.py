#!/usr/bin/python3
''' This script fetches https://alx-intranet.hbtn.io/status '''

from urllib import request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    with request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

        print(f'Body response:')
        print(f'    - type: {type(content)}')
        print(f'    - content: {content}')
        print(f'    - utf8 content: {utf8_content}')
