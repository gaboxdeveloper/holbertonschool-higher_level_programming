#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    delete = False
    for k, v in a_dictionary.items():
        if k == key:
            delete = True
    if delete is True:
        del a_dictionary[key]
    return a_dictionary
