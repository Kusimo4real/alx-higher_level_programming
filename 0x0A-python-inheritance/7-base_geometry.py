#!/usr/bin/python3
"""
This is a module that validate integer
"""


class BaseGeometry:
    """
    This is a class with method that validate integer
    """
    def area(self):
        """
        This is a method that does not implement method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This is the method that validate an integer
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError("{name} must be greater than 0")
