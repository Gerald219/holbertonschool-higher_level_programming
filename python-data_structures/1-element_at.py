#!/usr/bin/python3

def element_at(my_list, idx):
    # function to get item at position idx
    if idx < 0 or idx >= len(my_list):  # if position is invalid
        return None  # give back nothing
    return my_list[idx]  # give back the item at that position
