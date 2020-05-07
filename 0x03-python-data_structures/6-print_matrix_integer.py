#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    for row in range(rows):
        cols = len(matrix[row])
        for col in range(cols):
            if col != cols-1:
                print(matrix[row][col], end=' ')
            else:
                print(matrix[row][col])
