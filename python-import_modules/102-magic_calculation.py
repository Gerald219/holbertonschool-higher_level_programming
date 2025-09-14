#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:  # if a is smaller than b
        c = add(a, b)  # sum up a and b, save result in variable c
        for i in range(4, 6):  # produces 4 and 5
            c = add(c, i)  # sum up c and i, update c
        return c  # c + 4 + 5 = resulst stored in c
    else:  # if a is not smaller than b
        return sub(a, b)
