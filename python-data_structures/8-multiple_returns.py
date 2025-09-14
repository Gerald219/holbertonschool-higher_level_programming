#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)  # len() counts
    # if string is not empty, take first character, else take none
    first = sentence[0] if length > 0 else None
    return (length, first)  # give back both in a tuple
