#!/usr/bin/python3
"""
This module defines a function to add a new attribute to an object
if it's allowed.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to the object if possible.

    Args:
        obj: The object to which the attribute will be added.
        attr: The name of the new attribute.
        value: The value to assign to the new attribute.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
