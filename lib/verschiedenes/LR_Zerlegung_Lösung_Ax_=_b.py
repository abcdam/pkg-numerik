import numpy as np
import scipy.linalg

A = np.array([[1, 2, -1], [4, -2, 6], [3, 1, 0]])
b = np.array([9, -4, 9]) # ACHTUNG nur ein paar eckige Klammern
# P = Permutationsmatrix
# L = Linke untere Dreiecksmatrix
# R = Rechte obere Dreiecksmatrix
p, l, r = scipy.linalg.lu(A)

print('P = Permutationsmatrix\n', p,'\nL = Linke untere Dreiecksmatrix\n', l,'\nR = U = Rechte obere Dreiecksmatrix\n', r)
print('A\n', A)
print('L x R = P x A\n', l @ r)

y = scipy.linalg.solve(l, np.transpose(p)@b) # ACHTUNG p muss hier transponiert werden

print('Ly = Pb -> y =', y)
x = scipy.linalg.solve(r, y)
print('Rx = y -> x =', x)


print('Kontrolle: Ax=b:')
loesung = scipy.linalg.solve(A, b)
print('Ax = b -> x = ', loesung)
