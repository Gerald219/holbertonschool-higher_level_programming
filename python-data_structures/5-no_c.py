#!/usr/bin/python3

def no_c(my_string):  # remove all 'c' and 'C' from a string
    new_string = ""  # empty string
    for char in my_string:  # loop through each character
        if char != 'c' and char != 'C':  # do not print 'c' and 'C'
            new_string += char  # print the rest
    return new_string  # return the new string
