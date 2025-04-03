#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        first = None
        length = 0
        for i in sentence:
            length = length + 1
    else:
        length = 0
        for i in sentence:
            length = length + 1
        first = sentence[0]
    return length, first
