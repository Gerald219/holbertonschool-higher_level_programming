#!/usr/bin/python3  # run with Python

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):  # condition if invalid
        return my_list.copy()  # return a copy of the list unchanged
    new_list = my_list.copy()  # make a copy of the list
    new_list[idx] = element  # replace idx with element
    return new_list  # return the new list with the change
