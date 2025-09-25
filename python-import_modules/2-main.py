#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print("---- Test 1: no arguments ----")
    sys.argv = ["2-args.py"]
    exec(open("2-args.py").read())

    print("\n---- Test 2: one argument ----")
    sys.argv = ["2-args.py", "Hello"]
    exec(open("2-args.py").read())

    print("\n---- Test 3: many arguments ----")
    sys.argv = ["2-args.py", "Hello", "Welcome", "To", "The", "Best", "School"]
    exec(open("2-args.py").read())
