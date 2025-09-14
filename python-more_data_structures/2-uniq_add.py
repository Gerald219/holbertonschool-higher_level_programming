#!/usr/bin/python3


def uniq_add(my_list=[]):
    # eliminates duplicates and sums unique values in a list of integers
    uniq = set()  # set stores only unique values
    for v in my_list:  # v top go through list
        uniq.add(v)  # add each number (duplicates ignored)
    return sum(uniq)  # sum of all unique numbers
