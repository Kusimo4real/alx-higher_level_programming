#!/usr/bin/python3
"""Define a class square"""


class Square:
    """
    a class square that print a square
    """
    def __init__(self, size=0):
        """
        initialize a new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        a public area
        """
        return self.__size * self.__size
