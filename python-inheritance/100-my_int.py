#!/usr/bin/python3
"""
This module defines a rebel integer class MyInt
that inverts == and != operators.
"""


class MyInt(int):
    """
    MyInt is a subclass of int that inverts
    the behavior of == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the equality operator.

        Returns:
            bool: False if equal, True if not equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality operator.

        Returns:
            bool: True if equal, False if not equal.
        """
        return super().__eq__(other)
