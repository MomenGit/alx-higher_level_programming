#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for printed in range(0, x):
            print("{}".format(my_list[printed]), end='')
            printed = printed+1
    except:
        pass
    print()
    return printed
