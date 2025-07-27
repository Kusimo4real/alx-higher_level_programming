#!/usr/bin/python3
"""
This is a class mtList that inherits from list, it has a public
instance that prints the list, but in sorted ascending sort

"""


class MyList(list):
    """
    This is the inherited class from list that prints list but
    in a sorted manner
    """
    def print_sorted(self):
        """
        This is the function that prints the lists but in ascending manner
        """
        print(sorted(self))
