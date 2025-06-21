#!/usr/bin/python3


def append_write(filename="", text=""):
    """Appends text to a file and returns the number of characters written"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
