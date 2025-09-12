#!/usr/bin/python3

import hidden_4  # import the hidden_4 content

if __name__ == "__main__":  # run only if main file
    names = dir(hidden_4)  # use opener-list of names inside hidden_4
    for name in sorted(names):  # loop, lines them in order-A to Z
        if not name.startswith("__"):  # ignore special names
            print(name)  # show each allowed name
