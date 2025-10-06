#!/usr/bin/env python3
"""Defines the VerboseList class that extends list to print notifications on changes."""


class VerboseList(list):
    """A list that prints notifications when modified."""
    pass

    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extend the list and print how many items were added."""
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def pop(self, index=-1):
        """Pop an item (default: last) and print a notification."""
        item = self[index]  # look at what will be removed
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
