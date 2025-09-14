#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    # print list backwards
    if my_list is None:  # no list was given?
        return  # stop and do nothing!
    for i in reversed(my_list):  # use i to go through list backwards
        print("{:d}".format(i))  # print each item as an integer
