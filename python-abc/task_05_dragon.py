#!/usr/bin/env python3
"""Shows how a dragon can mix flying and swimming powers using mixins."""


class SwimMixin:
    """Gives the ability to swim."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Gives the ability to fly."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim, fly, and roar."""
    def roar(self):
        print("The dragon roars!")

