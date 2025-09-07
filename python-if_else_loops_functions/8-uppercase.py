#!/usr/bin/python3

def uppercase(str):  # Function
    result = ""  # Empty string to store
    for c in str:  # starts loop for each character
        if ord(c) >= 97 and ord(c) <= 122:  # lowercase
            result += chr(ord(c) - 32)  # converts to uppercase
        else:
            result += c  # add other characters unchanged
    print("{}".format(result))
