#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    # addition
    print("{} + {} = {}".format(a, b, add(a, b)))

    # subtraction
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # multiplication
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # division
    print("{} / {} = {}".format(a, b, div(a, b)))
