#!/usr/bin/python3
"""Inserts a line after every line that contains a given string in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts `new_string` after every line containing `search_string`."""
    lines = []

    with open(filename, "r") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, "w") as f:
        f.writelines(lines)
