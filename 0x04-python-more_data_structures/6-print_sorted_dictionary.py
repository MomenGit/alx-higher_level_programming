#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    print("Number: %d".format(len(sorted_keys)))
    for i in sorted_keys:
        print("{0}: {1}".format(i, a_dictionary[i]))
