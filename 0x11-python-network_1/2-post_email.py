#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
    from urllib import request, parse
    import urllib.request
    import sys
    data = {
        'email': sys.argv[2]
    }
    data = parse.urlencode(data)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
