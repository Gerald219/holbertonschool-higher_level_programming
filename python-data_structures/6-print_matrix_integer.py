#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):  # print a matrix of integers
    for row in matrix:  # go through each row
        for i, num in enumerate(row):  # gives position i and number num
            end_char = " " if i < len(row) - 1 else ""  
            # adds a space unless it’s the last number
            print("{:d}".format(num), end=end_char)  # print number
        print()  # new line after each row
