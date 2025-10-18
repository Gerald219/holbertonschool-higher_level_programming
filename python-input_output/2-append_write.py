#!/usr/bin/python3
"""Adds new text to the end of a normal text file (UTF-8)."""


def append_write(filename="", text=""):
    """Opens the file named in 'filename', adds the text at the end,
    and tells how many characters were added."""
    # "a" means add mode → it opens the file and starts writing at the end.
    # If the file doesn’t exist, Python creates it automatically.
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
