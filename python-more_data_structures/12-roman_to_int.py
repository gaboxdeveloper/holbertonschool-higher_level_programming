#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    retorno = 0
    for num in roman_string:
        if num == "I":
            retorno += 1
        if num == "V":
            retorno += 5
        if num == "X":
            retorno += 10
        if num == "L":
            retorno += 50
        if num == "C":
            retorno += 100
        if num == "D":
            retorno += 500
        if num == "M":
            retorno += 1000
    return retorno
