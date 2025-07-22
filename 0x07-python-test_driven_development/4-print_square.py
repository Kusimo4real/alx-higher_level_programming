#!/usr/bin/python3
"""
a module that prints a square with the character #
"""


def print_square(size):
    """
    a function that prints square with the characete #
    where size is the  length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
