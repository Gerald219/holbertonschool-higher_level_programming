#!/usr/bin/python3
"""
Main file for testing
"""

pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """Prints a triangle of integers"""
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

print_triangle(pascal_triangle(5))
