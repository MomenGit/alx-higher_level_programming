#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{:s}".format((chr(ord(c)-32))
              if (c >= 'a' and c <= 'z') else c), end='')
    print()


uppercase("best")
uppercase("Best School 98 Battery street")
