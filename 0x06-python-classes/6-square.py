#!/usr/bin/python3
"""
a class square
"""

class Square:
    """
    a class squre
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        this is the initialisation of the the code

        """
        self.size = size
        self.position = position

        @property
        def size(self):
            """
            a method size
            """
            return self._size

        @size.setter
        def size(self, value):
            """
            a method to set the value
            """
            if not isinstance(value, int):
                raise TypeError('size must be an integer')
            elif value < 0:
                raise ValueError('size must be >= 0')
            self.__size = value
        @property
        def position(self):
            """
            a method to se the value position
            """
            return self.__position
        
        @position.setter
        def position(self, value):
            if 
        
