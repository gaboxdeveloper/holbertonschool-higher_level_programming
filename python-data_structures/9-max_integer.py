#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_value = my_list[0]
    for b in my_list:
        if b > max_value:
            max_value = b
    return max_value
