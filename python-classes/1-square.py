#!/usr/bin/python3
"""Defines a class Square with a private instance attribute."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size: The size of the square (no type/value validation).
        """
        self.__size = size
