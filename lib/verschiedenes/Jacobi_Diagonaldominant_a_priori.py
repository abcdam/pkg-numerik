# Skript S. 65 - 68
# Jacobi- bzw. Ganzschrittverfahren
# Diagonaldominanz: a11 ≥ a 12 + a13, a22 ≥ a21 + a23, a33 ≥ a31 + a32
# Jedes Diagonalelement muss grösser als die Summe der Elemente in der Zeile oder Spalte sein.

import numpy as np

A = np.array([[8, 5, 2],
              [5, 9, 1],
              [4, 2, 7]], dtype='float64')
b = np.array([19, 5, 34], dtype=float).reshape(3, 1)
D = np.diagflat(np.diag(A), 0)
L = np.tril(A, k=0) - D
R = np.triu(A, k=0) - D
D_inverse = np.linalg.inv(D)
print('*** Jacobi- bzw. Gesamtschrittverfahren ***')
print('Iterationsschritt:'
      ' x**(m+1) = -D**(-1) x [(L + R) x x**(m) - b] = ')
print('A\n',A )
print('L\n', L)
print('D\n', D)
print('D_inverse, gebildet aus den Kehrwerten der Diagonale von D\n', D_inverse)
print('R\n', R)
print('\nL + R, A ohne die Diagonale\n', L + R)
print()
print('nD_inverse x (L + R), A ohne die Diagonale\n', L + R)
x0 = np.array([1, -1, 3], dtype=float).reshape(3, 1)
D_inv_LR = np.dot(D_inverse, L + R)
print('\nD_inverse * (L + R), (L + R) = A ohne die Diagonale\n', D_inv_LR)
D_inv_b = D_inverse.dot(b)
print('\nD_inverse * b\n', D_inv_b)
print('\nDie Iterationsformel lautet:')
print('x**(m+1) = - (D_inv * L + R) * x**(m) + (D_inv * b')
print('\nDie Iterationsformel mit den Werten lautet damit:')
print('x**(m+1) =\n-',D_inv_LR, '\n* x**(m) \n+', D_inv_b)


print("\n*** Jacobi-Verfahren Fixpunktiterationen: ***")
print('Die ersten Werte entsprechen x(1).\n')
print(x0)
xi_1 = x0
for i in range(3):
    xi = xi_1
    xi_1 = -1 * np.dot(D_inv_LR, xi) + D_inv_b
    print()
    print(xi_1)

print("\nExakte Lösung für Ax = b\nx =")
print(np.linalg.solve(A, b))

print("\n*** A priori Abschätzung: ***")
print('x_quer = tatsächlicher Wert.')
print('Es wird die unentlich Norm angewendet.')
print('||x_n - x_quer|| ≤ {||B||_n / 1 - ||B||} / ||x_1 -x_0||')
print('Berechne ||x_1 -x_0||')
print('Berechne ||B|| -> z.B. {Summe jeder Zeile, Summe jeder Zeile, Summe jeder Zeile}'
      '\n-> max{0.5, 30/a, 0.5}, wähle den maximalen Wert.'
      '\n-> 30/a für 30 < a < 60, *1/2* für a ≥ 60')

print("\n*** Berechne die Anzahl Schritte für eine bestimmte Toleranz ***")
print('z.B. bei a ≥ 60: Von oben: *1/2*')
print('||x_n - x_quer|| ≤ ((1/2)**n / 1/2) * a ≤ Toleranz')
print('Umformen nach n -> n = n(a) ≥ log(toleranz / 2a) / log(1/2)')
print('z.B. bei 30 < a < 60: Von oben: *30/a*, "1-30/a", weil das a innerhalb "< <" steht.')
print('||x_n - x_quer|| ≤ ((30/a)**n / (1 - 30/a)) * a ≤ Toleranz')
