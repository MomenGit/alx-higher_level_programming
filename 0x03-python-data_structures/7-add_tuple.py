#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup = [0, 0]

    for i in range(2):
        try:
            tup[i] = tup[i]+tuple_a[i]
        except IndexError:
            pass
        try:
            tup[i] = tup[i]+tuple_b[i]
        except IndexError:
            pass

    return (tup[0], tup[1])
