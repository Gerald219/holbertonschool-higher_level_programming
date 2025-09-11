#!/usr/bin/python3

from add_0 import add  # Activates the function

if __name__ == "__main__":  # checks if the file is the core one
    a = 1  # saves values in variables
    b = 2

    # format() result. add() does math. print() prints.
    print("{} + {} = {}".format(a, b, add(a, b)))
