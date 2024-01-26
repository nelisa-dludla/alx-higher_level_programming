#!/usr/bin/python3
'''
This script solves an interview question
'''

from requests import get
from sys import argv

if __name__ == '__main__':
    repo_name = argv[1]
    owner_name = argv[2]

    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    res = get(url)
    commits = res.json()
    sorted_commits = sorted(commits,
                            key=lambda x: x['commit']['author']['date'],
                            reverse=True)

    for commit in sorted_commits[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f'{sha}: {author_name}')
