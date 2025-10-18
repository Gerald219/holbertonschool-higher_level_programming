#!/usr/bin/python3
"""Reads and prints a UTF-8 text file."""


def read_file(filename=""):
    """Prints the contents of a text file."""
    # filename="" → default if no file name is given
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
