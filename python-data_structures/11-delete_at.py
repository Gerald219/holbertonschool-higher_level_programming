#!/usr/bin/python3

def delete_at(my_list=[], idx=0):  # deletes item at certain place
    if idx < 0 or idx >= len(my_list):  # check if index is invalid
        return my_list  # return list unchanged
    del my_list[idx]  # remove the item at position idx
    return my_list  # return the updated list
