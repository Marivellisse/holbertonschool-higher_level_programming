#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
Includes area and string representation.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square with equal width and height.
    """

    def __init__(self, size):
        """
        Initializes a square after validating size.

        Args:
            size (int): The size of the square sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area (size squared).
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            str: [Square] <size>/<size>
        """
        return "[Square] {0}/{0}".format(self.__size)
