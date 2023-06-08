#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv.pop(0)
    sum = 0
    if (len(argv)):
        for arg in argv:
            sum = sum + int(arg)
    print(sum)
