#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The function handles both int and float, and returns an int.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (converted to integers).
    
    Args:
        a: First number (int or float)
        b: Second number (int or float, defaults to 98)

    Returns:
        int: The sum of a and b after casting to integers

    Raises:
        TypeError: If either a or b is not an int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
