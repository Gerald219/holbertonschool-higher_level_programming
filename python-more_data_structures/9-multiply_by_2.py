#!/usr/bin/python3


def multiply_by_2(a_dictionary):  # double all values in dict
    new_dict = {}  # new empty dictionary
    for k, v in a_dictionary.items():  # loop through key and value
        new_dict[k] = v * 2  # keep the key, values are multiplied by 2
    return new_dict

