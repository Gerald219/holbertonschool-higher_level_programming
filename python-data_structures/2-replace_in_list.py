#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # function to replace item at a specific position
    if idx < 0 or idx >= len(my_list):  # if position is invalid
        return my_list  # print list unchanged, if not changes applied
    my_list[idx] = element  # put new element at position idx
    return my_list  # give back the updated list
