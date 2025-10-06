#!/usr/bin/env python3
"""Defines CountedIterator class that counts how many items were iterated."""


class CountedIterator:
    """Iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        """Initialize the iterator and set up the counter."""
        self.iterator = iter(iterable)  # create an iterator from any iterable
        self.count = 0  # start counter at zero
