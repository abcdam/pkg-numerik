import numpy as np
import scipy.linalg
from typing import Union

A = np.array([[1, 2, -1], [4, -2, 6], [3, 1, 0]])
b = np.array([9, -4, 9])
# Q = Q is an m×n matrix with Q x QT=I
# R = Rechte obere Dreiecksmatrix
# I = QQT=I
q, r = scipy.linalg.qr(A)
i = np.round(q@np.transpose(q), 1)

print('\nQ = Q is an m × n matrix with Q x QT=I\n',q ,'\nR = Rechte obere Dreiecksmatrix\n', r)
print('A\n', A)
print('I = Q x QT\n', i)
print('Q x R = A\n', np.round(q@r, 4))
print()
print("**** Calculation with Housholder matrices")

# **** Calculation with Housholder matrix")
def householder_vectorized(a):
    """Use this version of householder to reproduce the output of np.linalg.qr
    exactly (specifically, to match the sign convention it uses)

    based on https://rosettacode.org/wiki/QR_decomposition#Python
    """
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    tau = 2 / (v.T @ v)

    return v, tau


def qr_decomposition(A: np.ndarray) -> Union[np.ndarray, np.ndarray]:
    m,n = A.shape
    R = A.copy()
    Q = np.identity(m)

    for j in range(0, n):
        # Apply Householder transformation.
        v, tau = householder_vectorized(R[j:, j, np.newaxis])


        H = np.identity(m)
        H[j:, j:] -= tau * (v @ v.T)
        print('H', j+1, '= Q', j+1, '\n', H[j:, j:])
        print('Q', j+ 1, 'x A =', Q@A)
        R = H @ R
        Q = H @ Q
    return Q, R

Q, R = qr_decomposition(A)
print()
print('Kontrolle Q x R = A')
print('Calculatet A with Q x R =\n', np.round(q@r, 4))
print('Original A =\n', A)
print()
print("**** Calculation from Q and R with Housholder matrices")
print("**** Q from qr_decomposition")
print(np.round(Q, 4))
print()
print("**** R from qr_decomposition")
print(np.round(R, 4))

# Calculation of x
zwischenloesung = Q@b # ACHTUNG QT ist hier nicht mehr nötig
print('QT x b\n', zwischenloesung)
x = scipy.linalg.solve(R, zwischenloesung)
print('Rx = QT x b -> x\n', x)
