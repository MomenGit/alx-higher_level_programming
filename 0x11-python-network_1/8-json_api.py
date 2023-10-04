#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""

if __name__ == '__main__':
    import requests
    import sys
    if len(sys.argv) >= 2:
        q = sys.argv[1]
    else:
        q = ""
    res = requests.post('http://0.0.0.0:5000/search_user', {'q': q})
    try:
        body = res.json()
        if len(body) == 0:
            print("No result")
        else:
            print("[{}] {}".format(body.get('id'), body.get('name')))
    except Exception as e:
        print("Not a valid JSON")
