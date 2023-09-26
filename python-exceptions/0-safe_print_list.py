#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            if i == x - 1:
                print(my_list[i])
            else:
                print(my_list[i], end='')
        return x
    except Exception:
        print("")
        return i
