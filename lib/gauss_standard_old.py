import numpy as np


def gauss(A, b):
    """

    :param A: Matrix A
    :param b: Vektor b
    :return: Determinante A, x (Lösung)
    """
    # turn inputs into floats
    A = A.astype(float)
    b = b.astype(float)

    n = A.shape[0]
    Ab = np.append(A, b, axis=1)

    # iterate over columns
    for i in range(n):
        # check if diagonal element A[i][i] is 0
        if A[i][i] == 0:
            # check if there are only 0s below diag element in this column
            if check_regularity(Ab, i) == -1:
                raise Exception('Die Matrix ist nicht regulaer!')
            # exchange row with the first element !=0
            else:
                Ab = exchange_rows(Ab, i, check_regularity(Ab, i))
        Ab = make_column_below_zero(Ab, i)
    return [get_determinant(Ab), solve(Ab)]


def check_regularity(A, j):
    n = A.shape[0]
    for i in range(j + 1, n):
        if A[i][j] != 0:
            return i
    return -1


def exchange_rows(A, i, j):
    AC = np.copy(A)
    n = A.shape[0]
    for k in range(n + 1):
        AC[i][k] = A[j][k]
        AC[j][k] = A[i][k]
    return AC


def make_column_below_zero(A, j):
    n = A.shape[0]
    AC = np.copy(A)
    for i in range(j + 1, n):
        x = -AC[i][j] / A[j][j]
        AC[i, :] = A[i, :] + x * A[j, :]
    return AC


def get_determinant(A):
    det = 1
    n = A.shape[0]
    for i in range(n):
        det = det * A[i][i]
    return det


def solve(A):
    n = A.shape[0]
    x = np.zeros(n, np.float64)
    i = n - 1
    while i >= 0:
        sum = 0
        for j in range(n):
            sum += A[i][j] * x[j]
        x[i] = 1 / A[i][i] * (A[i][n] - sum)
        i -= 1
    return x

