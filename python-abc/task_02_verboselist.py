#!/usr/bin/env python3
"""Defines the VerboseList class that extends list to print notifications on changes."""


class VerboseList(list):
    """A list that prints notifications when modified."""
    pass

    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")


