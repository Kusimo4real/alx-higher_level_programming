#!/usr/bin/python3
"""
This is a module that returns true id the object is exactly
an instance of the specified class therewise it False
"""


def is_same_class(obj, a_class):
    """ This is a function that that return True if the object is exactly
    an instance of the object
    """
    return type(obj) is a_class
