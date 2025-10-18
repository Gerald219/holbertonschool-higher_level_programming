#!/usr/bin/python3
"""Writes text into a UTF-8 file."""


def write_file(filename="", text=""):  # text is used to hold the string
    """Writes a string to a text file and returns character count."""
    with open(filename, "w", encoding="utf-8") as f:  # w is for writting into
        return f.write(text)
