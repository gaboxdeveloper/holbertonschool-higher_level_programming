#!/usr/bin/python3
"""lalala"""


def is_same_class(obj, a_class):
    """returns True if the objetct
    is exactly an instance of the
    specified class, otherwise False"""
    if isinstance(obj, a_class):
        return True
    return False
