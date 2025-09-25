#!/usr/bin/python3
from add_0 import add  # import the add function

if __name__ == "__main__":  # only run if this is the main file
    a = 1  # first number stored in a
    b = 2  # second number stored in b
    # format fills the blanks, add does the math, prints
    print("{} + {} = {}".format(a, b, add(a, b)))
