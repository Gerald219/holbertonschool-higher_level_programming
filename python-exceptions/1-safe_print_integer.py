#!/usr/bin/python3


def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # print value as an integer
        return True  # success: it printed
    except (ValueError, TypeError):
        return False  # not an int-format value
