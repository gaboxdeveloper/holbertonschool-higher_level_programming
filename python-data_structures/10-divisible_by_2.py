#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = []
    for num in my_list:
        multiple2 = (num % 2 == 0)
        result_list.append(multiple2)
    return result_list
