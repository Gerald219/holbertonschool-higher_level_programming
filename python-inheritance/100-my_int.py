#!/usr/bin/python3
"""MyInt class that flips equality behavior."""


class MyInt(int):
    """A rebel version of int that inverts == equal to and not !=."""

    def __eq__(self, other):
        """Return True when values are not equal."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return True when values are equal."""
        return super().__eq__(other)
