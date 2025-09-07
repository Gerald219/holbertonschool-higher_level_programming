#!/usr/bin/python3

for i in range(97, 123):
    if chr(i) != 'q' and chr(i) != 'e':  # excludes 'q' and 'e'
        print("{}".format(chr(i)), end="")
