#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0  # return 0 if input is not a string

    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }  # map each Roman letter to its number

    total = 0  # result starts at 0
    prev = 0   # tracks the last value we saw

    for ch in reversed(roman_string):  # loop from right to left
        value = roman_map.get(ch, 0)  # get number for symbol
        if value < prev:  # if smaller than last number
            total -= value  # subtract it
        else:
            total += value  # else add it
        prev = value  # update last number
    return total  # return the final result
