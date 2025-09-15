#!/usr/bin/python3


def best_score(a_dictionary):
    # find key with biggest value
    if not a_dictionary:  # verify, is dict empty?
        return None  # if empty print nothing
    best = max(a_dictionary, key=a_dictionary.get)  # key with biggest value
    # max() finds largest key
    return best
