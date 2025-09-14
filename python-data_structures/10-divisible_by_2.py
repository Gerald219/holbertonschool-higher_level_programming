#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result = []  # start empty list to store into it
    for num in my_list:  # use num to go though each like i
        if num % 2 == 0:  # % gives remainder, 0 means divisible by 2
            result.append(True)  # adds a new item to the end
        else:  # if not divisible by 2
            result.append(False)  # add False if number is odd
    return result  # give back list of True/False
