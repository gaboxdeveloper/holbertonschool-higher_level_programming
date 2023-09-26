#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    retorno = 0
    for num in range(len(roman_string)):
        if roman_string[num] == "I":
            if num == (len(roman_string) - 1):
                retorno += 1
            elif roman_string[num + 1] == "V" or roman_string[num + 1] == "X":
                retorno -= 1
            else:
                retorno += 1
        if roman_string[num] == "V":
            retorno += 5
        if roman_string[num] == "X":
            retorno += 10
        if roman_string[num] == "L":
            retorno += 50
        if roman_string[num] == "C":
            retorno += 100
        if roman_string[num] == "D":
            retorno += 500
        if roman_string[num] == "M":
            retorno += 1000
    return retorno
