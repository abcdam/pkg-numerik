# Eigenwert & -vektoren
# =====================
#
# Über die :doc:`Normberechnung <01-norm.py>` hinaus stellt die
# :file:`numpy.linalg` Erweiterung auch Funktionen zur Berechnung von
# Eigenwerten und Eigenvektoren bereit.
#
# Wir haben wieder eine zufällige :math:`100\times 100` Matrix::

import numpy as np
import numpy.linalg as linalg

# A = np.random.rand(3,3)
A = np.array([[1, 1, 0], [3, -1, 2], [2, -1, 3]])
det = np.linalg.det(A)
print('Matrix A\n', np.round(A, 5))
print('')
print('Determinante =', det)
print('')

# Eigenwerte und Eigenvektoren berechnen.
# Eigenwerten 'ew', Eigenvektoren 'ev'

ew, ev = linalg.eig(A)
print('Eigenwerte:')
print(ew)
print('')
print('Eigenvektoren: Spaltenweise x1, x2, x3 herauslesen:')
print(np.round(ev, 4))
print('')

# Betragsmäßig kleinsten und größten Eigenwert und den dazugehörigen Eigenvektor bestimmen.
# Beträge der (i.d.R. komplexen) Eigenwerte:

ew_abs = np.abs(ew)

# Mit 'argmax'/'argmin' wird der Index des maximalen/minimalen Eigenwerts berechnet.

ew_max = np.argmax(ew_abs)
ew_min = np.argmin(ew_abs)

# Ergebnisse ausgeben.

print("max Eigenwert ", ew[ew_max])
print("  + Eigenvektor ", ev[ew_max])
print('')
print("min Eigenwert ", ew[ew_min])
print("  + Eigenvektor ", ev[ew_min])

# Iteratives Verfahren
# Startvektor x
v0 = np.array([1,0,0], dtype=np.float64)
print('v0 = ', v0)

lam0 = 1.0
# Abbruch sobald die Fehlertoleranz unterschritten wird.
tol = 1e-2
# Anzahl der Iterationen anpassen, falls diese nichtr ausreichen
maxiter = 50
iter = 0
# Iteration
while True:
    w = A @ v0
    print('w = ', w)
    v1 = w / np.linalg.norm(w)
    lam1 = np.dot(v0, w) / np.dot(v0,v0)
    iter += 1

    print('Iter = ', iter)
    print('v1 = ', v1)
    print('lam1 = ', lam1)

    if np.abs(lam1-lam0) < tol and np.linalg.norm (v1-v0) < tol:
        break
    elif iter > maxiter:
        raise Exception('Keine Konvergenz')

    v0 = v1
    lam0 = lam1

print('v = ', v0)
print('lam = ', lam0)
