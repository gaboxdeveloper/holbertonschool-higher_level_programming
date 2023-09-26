#!/usr/bin/python3
def best_score(a_dictionary):
    comparable = 0
    retorno = ""
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > comparable:
                retorno = k
                comparable = v
    else:
        return None
    return retorno
