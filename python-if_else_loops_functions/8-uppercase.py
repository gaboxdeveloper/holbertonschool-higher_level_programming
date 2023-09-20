#!/usr/bin/python3
def uppercase(str):
    result = []
    for char in str:
        upper = ord(char)
        if (96 < upper < 123):
            upper -= 32
        result.append(chr(upper))
    print("".join(result))
