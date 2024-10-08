#!/usr/bin/python3

"""
this is a square that defines a square
"""


class Square:
    """ This is a class square"""
    def __init__(self, size=0):
        """Initialize a new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
