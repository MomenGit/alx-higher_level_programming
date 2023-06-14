#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    avg = 0
    weights = 0
    for tup in my_list:
        avg = avg + tup[0] * tup[1]
        weights = weights + tup[1]

    return avg / weights
