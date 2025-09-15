#!/usr/bin/python3

def safe_print_division(a, b):
    result = None  # start no answer
    try:
        result = a / b  # try dividing a by b
    except ZeroDivisionError:  # if b is 0
        result = None  # keep result as None
    finally:
        # always runs, no matter what, and prints
        print("Inside result: {}".format(result))
    return result  # result
