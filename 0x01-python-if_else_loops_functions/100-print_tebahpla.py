#!/usr/bin/python3

def print_ascii():
    for i in range(122, 96, -1):
        if i % 2 == 0:
            print((chr(i)), end='')
        else:
            print((chr(i-32)), end='')


print_ascii()
