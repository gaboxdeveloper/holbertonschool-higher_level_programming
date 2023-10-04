#!/usr/bin/python3
"""Public instance method: def print_sorted(self):
that prints the list, but sorted (ascending sort)
You can assume that all the elements of the list
will be of type int"""


class MyList(list):
    """class inherited
    from the list class"""
    def print_sorted(self):
        """Print the list elements in ascending sorted order."""
        if all(isinstance(i, int) for i in self):
            print(sorted(self))
