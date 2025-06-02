#!/usr/bin/python3
"""
This module defines the function `lookup` that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of attributes and methods available in the given object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of attribute and method names.
    """
    return dir(obj)
