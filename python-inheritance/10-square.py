#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
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
