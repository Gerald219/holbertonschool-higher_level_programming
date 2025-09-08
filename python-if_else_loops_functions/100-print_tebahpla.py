#!/usr/bin/python3
for i in range(122, 96, -1):  # loop start
    if (122 - i) % 2 == 0:  # even or odd?
        print("{}".format(chr(i)), end="")  # chr(i)converts the ASCII to letter
    else:
        print("{}".format(chr(i - 32)), end="")
