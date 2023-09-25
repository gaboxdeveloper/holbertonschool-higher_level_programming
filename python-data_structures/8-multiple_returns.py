#!/usr/bin/python3
def multiple_returns(sentence):
    largo = len(sentence)
    if sentence == None:
        pchar = None
    else:
        for i in sentence:
            pchar = sentence[0]
    return largo pchar
