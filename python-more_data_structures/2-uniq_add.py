#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set()
    result = 0
    for num in my_list:
        if num not in new_set:
            result += num
            new_set.add(num)
    return result
