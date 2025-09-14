#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None  # empty list, nothing to compare

    max_val = my_list[0]  # start by assuming first number is biggest
    for num in my_list:   # go through each number in the list
        if num > max_val:  # compare current number, is bigger than max_val?
            max_val = num  # mark it as new max_val, biggest
    return max_val
