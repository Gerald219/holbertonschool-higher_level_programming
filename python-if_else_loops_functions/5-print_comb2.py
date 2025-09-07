#!/usr/bin/python3
for i in range(100):  # goes from 0 to 99
    if i < 99:  # if not the last number print with a comma and space
        print("{:02d}, ".format(i), end="")  #
    else:
        print("{:02d}".format(i))
