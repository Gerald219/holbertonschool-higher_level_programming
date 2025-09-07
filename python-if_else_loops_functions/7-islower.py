#!/usr/bin/python3

def islower(c):
    # returns True if c is lowercase, False otherwise
    return ord(c) >= 97 and ord(c) <= 122
    # Alternatively, you can use: return 'a' <= c <= 'z'
