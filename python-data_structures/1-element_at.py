#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        for n in range(idx + 1):
            if n == idx:
                return my_list[n]
