#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Returns a list of lists of integers representing the Pascal's triangle'''
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # The first element of each row is always 1
        if triangle:
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j + 1]
                       for j in range(len(last_row) - 1)])
            row.append(1)  # The last element of each row is always 1
        triangle.append(row)

    return triangle
