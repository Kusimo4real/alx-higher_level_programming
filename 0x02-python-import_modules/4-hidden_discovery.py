#!/usr/bin/python3
"""
    a program that prints all the names deifned by the compiled module hidden_4.pyc
"""
if __name__ == "__main":
    import hidden_4
    names=dir(hidden_4)
    for i in names:
        if i.startwith("_"):
            continue
        print(i)

