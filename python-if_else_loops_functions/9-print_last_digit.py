#!/usr/bin/python3

def print_last_digit(number):
    last_digit = abs(number) % 10  # Gets the last digit
    print("{}".format(last_digit), end="")  # prints
    return last_digit
