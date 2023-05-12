#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:

        for col_index in range(len(row)):

            if col_index == len(row) - 1:
                print("{:d}".format(row[col_index]), end="")

            else:
                print("{:d} ".format(row[col_index]), end="")

        print()
