#!/usr/bin/python3
"""
takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""

if __name__ == '__main__':
    import requests
    import sys
    from requests.auth import HTTPBasicAuth
    url = "https://api.github.com/user"
    username = sys.argv[1]
    token = sys.argv[2]
    auth = HTTPBasicAuth(username, token)

    res = requests.get(url, auth=auth)
    try:
        body = res.json()
        print("{}".format(body.get('id')))
    except Exception as e:
        print(None)
