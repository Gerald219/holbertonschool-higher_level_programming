#!/usr/bin/python3

from calculator_1 import add, sub, mul, div  # import python math functions
import sys  # toolbox for argv and exit

if __name__ == "__main__":  # only run if this is the main file
    if len(sys.argv) != 4:  # must give exactly 3 arguments
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)  # exit if code wrong

    a = int(sys.argv[1])  # first number
    operator = sys.argv[2]  # the math symbol
    b = int(sys.argv[3])  # second number

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
        sys.exit(1)  # exit with error code if wrong operator
