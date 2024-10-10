#!/usr/bin/python3
"""
Define a class square

"""


class Square:
    """
    a class square
    """

    def __init__(self, size=0):
        """
        Initialize a new square
        """
        self.size = size

    @property
    def size(self):
        """
        a method size
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        a setter to set a size
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        this is the method that define a square
        """
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print('')

        for i in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
