#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv.pop(0)
    if (len(argv) == 0):
        print("0 arguments.")
    else:
        print("{:d} argument{}:".format(
            len(argv), 's'if (len(argv) > 1)else ''))
        for i, arg in enumerate(argv, 1):
            print("{:d}: {:s}".format(i, arg))
