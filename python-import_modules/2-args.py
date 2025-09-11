#!/usr/bin/python3

import sys  # read command line args

if __name__ == "__main__":  # only runs if this is the main file
    argv = sys.argv[1:]  # skip script name, keep the rest
    count = len(argv)  # number of arguments

    if count == 0:  # no arguments
        print("0 arguments.")
    elif count == 1:  # one argument
        print("1 argument:")
    else:  # more than one arg
        print("{} arguments:".format(count))  # show how many

    for idx, arg in enumerate(argv, start=1):  # go through each
        print("{}: {}".format(idx, arg))  # print the number/item
