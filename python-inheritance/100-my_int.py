#!/usr/bin/python3
"""Module for MyInt class that inverts equality operators."""


class MyInt(int):
    """MyInt is a rebel that inverts == and !=."""

    def __eq__(self, other):
        """Inverts == to behave like !=."""
        return int(self) != other

    def __ne__(self, other):
        """Inverts != to behave like ==."""
        return int(self) == other
