#!/usr/bin/python3
'''
This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
'''

from requests import get
from sys import argv

if __name__ == '__main__':
    url = f'https://api.github.com/user'
    username = argv[1]
    token = argv[2]
    headers = {'Authorization': f'Bearer {token}'}

    res = get(url, headers=headers)
    user_data = res.json()
    user_id = user_data.get('id')

    print(user_id)
