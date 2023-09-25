#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = {}
    for i in sorted(a_dictionary):
        new_dict += [i]
    return new_dict
