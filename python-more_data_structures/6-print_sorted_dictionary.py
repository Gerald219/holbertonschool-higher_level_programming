#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for k in sorted(a_dictionary):  # sorted() sorts keys/lebels alphabetically
        print(f"{k}: {a_dictionary[k]}")  # print key/label and its value
