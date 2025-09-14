#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    res = []  # new matrix to fill
    for row in matrix:  # use row to go through one at a time
        new_row = []  # start an empty row for the squared values
        for v in row:  # each number in the row
            new_row.append(v * v)  # square it sand store it
        res.append(new_row)  # add the new row
    return res  # give back the new matrix
