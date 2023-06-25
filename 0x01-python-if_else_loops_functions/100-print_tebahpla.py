#!/usr/bin/python3
for i in range(97+25, 96, -1):
    print("{:s}".format(chr((i) if (i % 2 == 0) else (i-32))), end='')
