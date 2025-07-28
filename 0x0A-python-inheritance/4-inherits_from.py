#!/usr/bin/python3
"""
a module that returns True if the object is an instance of a class
that inherited(directly of indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    a function that returns True id the object  is an instance of a class
    that inherited from the specified class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
