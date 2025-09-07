#!/usr/bin/python3
for i in range(100):  # prints numbers from 0 to 99
    print("{:02d}".format(i), end=", " if i < 99 else "\n")
