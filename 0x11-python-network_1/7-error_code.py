#!/usr/bin/python3
"""
takes in a URL, sends a request and displays the body of the response
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""

if __name__ == '__main__':
    import requests
    import sys
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
