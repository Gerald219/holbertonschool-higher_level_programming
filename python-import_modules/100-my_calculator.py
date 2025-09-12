#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    if len(argv) != 4:  # must give exactly 3 arguments
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        raise SystemExit(1)  # exit if code wrong

    a = int(argv[1])  # first number
    operator = argv[2]  # the math symbol
    b = int(argv[3])  # second number

    if operator == "+":  # check for addition
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == "-":  # check for subtraction
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == "*":  # check for multiplication
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == "/":  # check for division
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:  # anything else is not allowed
        print("Unknown operator. Available operators: +, -, * and /")
        raise SystemExit(1)  # exit with error code if wrong operator
