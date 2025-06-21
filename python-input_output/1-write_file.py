#!/usr/bin/python3
"""Function that writes text to a UTF-8 text file
and returns character count.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns
    number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        chars_written = f.write(text)
    return chars_written
