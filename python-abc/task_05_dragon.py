#!/usr/bin/python3
"""Task 5 - Dragon with mixins."""


class SwimMixin:
    """Mixin that adds swimming behavior."""
    def swim(self):
        """Print a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior."""
    def fly(self):
        """Print a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon that can swim, fly, and roar."""
    def roar(self):
        """Print a roaring message."""
        print("The dragon roars!")
