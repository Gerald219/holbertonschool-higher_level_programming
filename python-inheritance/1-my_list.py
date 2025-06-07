#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Custom list class that adds a sorted print method."""

    def print_sorted(self):
        """Prints the list sorted in ascending order without changing it."""
        print(sorted(self))
