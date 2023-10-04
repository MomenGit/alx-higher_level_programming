#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""

if __name__ == '__main__':
    import requests
    import sys
    q = sys.argv[1] if sys.argv[1] is not None else ""
    res = requests.post('http://0.0.0.0:5000/search_user', {'q': q})
    try:
        json = res.json()
        if json is None:
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except Exception as e:
        print("Not a valid json")
