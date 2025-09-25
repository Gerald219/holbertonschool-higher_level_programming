#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print("---- Test 1: no arguments ----")
    sys.argv = ["3-infinite_add.py"]
    exec(open("3-infinite_add.py").read())

    print("\n---- Test 2: two arguments ----")
    sys.argv = ["3-infinite_add.py", "79", "10"]
    exec(open("3-infinite_add.py").read())

    print("\n---- Test 3: many arguments ----")
    sys.argv = ["3-infinite_add.py", "79", "10", "-40", "-300", "89"]
    exec(open("3-infinite_add.py").read())

    print("\n---- Test 4: very large numbers ----")
    sys.argv = ["3-infinite_add.py",
                "1111111111111111111111111111111111",
                "9999999999999999999999999999999999"]
    exec(open("3-infinite_add.py").read())
