#!/usr/bin/python3
"""Module to read and print a text file using UTF-8 encoding."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
