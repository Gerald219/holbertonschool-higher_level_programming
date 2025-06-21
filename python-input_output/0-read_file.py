#!/usr/bin/python3
"""Reads a UTF-8 text file and prints its content to stdout."""

def read_file(filename=""):
    """Prints the contents of a text file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
