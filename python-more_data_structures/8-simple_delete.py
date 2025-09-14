#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):  # delete a key if it exists
    if key in a_dictionary:  # check if key/label is present?
        del a_dictionary[key]  # delete that key and its value
    return a_dictionary  # give back the updated dictionary
