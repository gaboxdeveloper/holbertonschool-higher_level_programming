#!/usr/bin/python3
"""lalala"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False."""
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
