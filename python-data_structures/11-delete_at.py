#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    else:
        new_list = my_list.copy()
        new_list -= new_list[idx]
        return new_list
