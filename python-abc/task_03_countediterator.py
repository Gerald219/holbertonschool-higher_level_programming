#!/usr/bin/env python3
"""CountedIterator class that counts how many items were iterated."""


class CountedIterator:
    """Iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        """Prepare the iterator and start the counter."""
        self.iterator = iter(iterable)  # turn the list into a iterator
        self.count = 0  # starting position

    def __iter__(self):
        """Let Python know this object can be looped through."""
        return self

    def __next__(self):
        """Get the next item and increase the counter."""
        try:
            item = next(self.iterator)  # get next item from list
        except StopIteration:
            raise  # stop ->there are no items left
        else:
            self.count += 1  # add +1 to counter
            return item  # return the current item

    def get_count(self):
        """Return how many items have been taken so far."""
        return self.count
