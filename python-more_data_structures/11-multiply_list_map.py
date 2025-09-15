#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):  # multiply list by number
    return list(map(lambda x: x * number, my_list))
    # lambda-mini function inside another functionS
    # map() applies lambda to each item
    # list() turns result from map object back into a list
