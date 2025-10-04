#!/usr/bin/python3
"""a list that can also print itself sorted."""


class MyList(list):
    """A list with one extra trick."""

    def print_sorted(self):
        """Show the list in order"""
        print(sorted(self))
