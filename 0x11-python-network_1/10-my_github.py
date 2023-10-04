#!/usr/bin/python3
"""Docs"""

if __name__ == '__main__':
    import requests
    import sys
    headers = {
        "Authorization": "Bearer {}".format(sys.argv[2]),
        "X-GitHub-Api-Version": "2022-11-28"
    }
    res = requests.get("https://api.github.com/{}".format(sys.argv[1]))
    try:
        body = res.json()
        print("{}".format(body.get('id')))
    except Exception as e:
        print(None)
