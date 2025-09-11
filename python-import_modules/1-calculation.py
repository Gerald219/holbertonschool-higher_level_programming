#!/usr/bin/python3  # tells computer "run this in Python"

from calculator_1 import add, sub, mul, div  # import math tools

if __name__ == "__main__":  # run only if main file
    a = 10  # first number
    b = 5   # second number

    # addition with add, format, print
    print("{} + {} = {}".format(a, b, add(a, b)))

    # subtraction with sub, format, print
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # multiplication with mul, format, print
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # division with div, format, print
    print("{} / {} = {}".format(a, b, div(a, b)))
