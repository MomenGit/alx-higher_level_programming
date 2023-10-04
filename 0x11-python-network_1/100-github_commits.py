#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository “rails”
by the user “rails”
"""

if __name__ == '__main__':
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    res = requests.get(url, params={'per_page': 10})
    try:
        commits = res.json()
        for commit in commits:
            print("{}: {}".format(commit.get('sha'),
                  commit.get('commit').get('author').get('name')))
    except Exception as e:
        print(None)
