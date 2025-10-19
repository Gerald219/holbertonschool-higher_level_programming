#!/usr/bin/python3
"""Insert a line of text to a file after each line containing a string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after every line that has the search_string."""
    # open file and read all lines
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # open file again to rewrite it
    with open(filename, "w", encoding="utf-8") as f:
        # go through each line
        for line in lines:
            f.write(line)
            # if the line has the search word, add the new one right after
            if search_string in line:
                f.write(new_string)
