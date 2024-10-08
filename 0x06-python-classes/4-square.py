#!/usr/bin/python3

"""
This is a class that defines a square
"""


class Square:
    """
    a class square that print a square
    """
    def __init__(self, size=0):
        """
        initialize a new square
        """
        self.size = size

    @property
    def size(self):
        """
        get and set the current size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        return the area of a square
        """
        return self.__size * self.__size
