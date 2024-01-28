#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            sem = chr(ord(i) - 32)
        else:
            sem = i
        print("{}".format(sem), end=n'')
    print("{}".format(""))
