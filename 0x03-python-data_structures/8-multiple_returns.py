#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        first = None
        return first
    length = 0
    for i in sentence:
        length = length + 1
    first = sentence[0]

    return length, first
