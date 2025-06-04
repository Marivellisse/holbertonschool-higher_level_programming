#!/usr/bin/python3
"""Module that writes a string to a text file (UTF8) and returns the number of characters written."""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The text to write to the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
