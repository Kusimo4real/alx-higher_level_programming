#!/usr/bin/python3
"""
a module of a empty base gometry that raises an exception
"""


class BaseGeometry:
    """
    a class that raises an exception
    """
    def area(self):
        """
        a public method that raises an excpetion
        """
        raise Exception("area() is not implemented")
