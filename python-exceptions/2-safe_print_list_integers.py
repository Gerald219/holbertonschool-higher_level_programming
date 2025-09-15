#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0  # how many ints we printed
    for i in range(x):  # i goes through each
        try:
            print("{:d}".format(my_list[i]), end="")  # print if int-like
            count += 1  # count it
        except (ValueError, TypeError):  # not an int for {:d} so skip
            continue
    print()  # newline at end
    return count  # number of ints printed
