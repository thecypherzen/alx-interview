#!/usr/bin/python3
"""2D array rotation script
"""


def rotate_2d_matrix(matrix):
    """A function that rotates a 2D n x n array
    90deg clockwise

    Params:
       - matrix(list[list[Any]]): n x n matrix
    Returns:
       - None
    """
    # for clockwise rotation, swap rows
    # for anti-clockwise rotation, swap columns
    N = len(matrix)
    i = 0
    j = N - 1
    # swap rows
    while i < j:
        temp = matrix[i]
        matrix[i] = matrix[j]
        matrix[j] = temp
        i += 1
        j -= 1
    # transpose matrix
    i = 0
    while i < N:
        n = len(matrix[i])  # this avoids error for nxm matrix
        j = i + 1
        while j < n:
            matrix[i][j] = matrix[i][j] ^ matrix[j][i]
            matrix[j][i] = matrix[i][j] ^ matrix[j][i]
            matrix[i][j] = matrix[i][j] ^ matrix[j][i]
            j += 1
        i += 1
