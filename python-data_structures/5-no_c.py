#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for let in my_string:
        if let != 'c' or let != 'C':
            new_string += let
    return new_string
