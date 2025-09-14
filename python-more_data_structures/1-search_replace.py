#!/usr/bin/python3


def search_replace(my_list, search, replace):
    res = []  # create empty list to fill
    for v in my_list:  # use v to go through each
        if v == search:  # v matches search value?
            res.append(replace)  # put replacement in the new list
        else:  # if it does not match
            res.append(v)  # keep unchanged
    return res  # return the new list
