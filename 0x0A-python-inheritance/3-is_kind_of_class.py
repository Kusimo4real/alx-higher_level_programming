#!/usr/bin/python3
"""
a module that returns True if the object is an instance of
or if the object is an instance of a class that inherited
from the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    This is a function that returns true if the object is an instance of
    if the object is an instance of a class that inherited from otherwise
    false
    """
    return (isinstance(obj, a_class))

