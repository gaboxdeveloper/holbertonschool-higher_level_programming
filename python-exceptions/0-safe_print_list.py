#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for i in range(x):
            pepito = my_list[i]
            print("{}".format(pepito), end='')
            printed += 1
        print()
    except IndexError:
        print()
    return printed
