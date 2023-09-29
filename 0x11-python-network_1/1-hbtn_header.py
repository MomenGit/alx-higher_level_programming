#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
    import urllib.request
    import sys
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        print(response.headers.__getitem__('X-Request-Id'))
