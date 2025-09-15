#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0  # how many printed, start at position 0
    for i in range(x):  # loop through it with i, range=loop counter
        try:
            print(my_list[i], end="")  # print item with no space
            count += 1  # count printed item
        except IndexError:  # list too short
            break  # stop loop
    print()  # newline at end
    return count  # real number of items printed
