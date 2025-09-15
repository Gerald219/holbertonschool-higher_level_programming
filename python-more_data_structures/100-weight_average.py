#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:  # empty list case
        return 0
    total = 0
    weight_sum = 0
    for score, weight in my_list:  # go through each tuple
        total += score * weight  # add weighted score
        weight_sum += weight  # add weight
    return total / weight_sum  # compute average
