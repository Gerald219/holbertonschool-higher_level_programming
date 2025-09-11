#!/usr/bin/python3

import sys  # sys gives access to command line args

if __name__ == "__main__":  # run the main file
    argv = sys.argv[1:]  # skip script name
    total = 0  # start from
    for arg in argv:  # loop argv the box holding args
        total += int(arg)  # turn text into number, sum it
    print(total)  # show the final sum
