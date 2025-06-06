#!/usr/bin/python3
"""
Module that defines the function read_file.
Reads the content of a UTF-8 encoded text file and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
