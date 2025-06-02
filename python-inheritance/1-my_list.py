#!/usr/bin/python3
"""
This module defines a subclass of list called MyList
with a method to print the list sorted.
"""


class MyList(list):
    """
    A subclass of list with a custom method to print
    the elements in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list's elements in ascending sorted order.
        The original list remains unchanged.
        """
        print(sorted(self))
