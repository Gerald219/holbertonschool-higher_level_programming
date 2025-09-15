#!/usr/bin/python3
"""
This module defines the function text_indentation.
It prints text with 2 new lines after each '.', '?' or ':'.
"""


def text_indentation(text):
    """
    Print text with 2 new lines after '.', '?' or ':'.

    Args:
        text (str): The text to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
