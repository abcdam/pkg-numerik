# Skript S. 27
# 1. Fragen:
# Gibt es eine Nullstelle für f(x), wenn ja in welchem Bereich?
# Gibt es mehrere Nullstellen?
# Wie lautet die Fixpunktgleichung?
# z.B. f(x) = x**3 - x + 0.3 = 0 -> F(X_quer) = x**3 + 0.3 = x oder F(X_quer) = sqrt(x - 0.3) = x
# Startwerte für x0 herraussuchen (entspricht den Werten in der Nähe der Nullstellen)
# Falls |F'(x_quer)| < 1: anziehnder Fixpunkt
# Falls |F'(x_quer)| > 1: abstossender Fixpunkt

# Welche Nullstellen gibt es?
import sympy.solvers as sol
import sympy as syp
x = syp.Symbol('x')
# f = syp.cos(x)
f = x**3 - x + 0.3
print('f(x)', f)
print('Nullstellen: ', sol.solve(f, x))
# Wie lautet die Ableitung der Fixpunktgleichung?
# Fixpunktgleichung, aus f umgeformt
F = x**3 + 0.3
x0 = 1
print('Bestimme, ob die Werte für x0 in der Ableitung der Fixpunktgleichng < oder > 1 sind:')
print('Fixpunktgleichung = ', F)
print('Setze die Werte für x0 (mögliche Nullstellen) ein: ')
print('F_Ableitung =', syp.diff(F, x))
print("Falls |F'(x0)| < 1: anziehender Fixpunkt")
print("Falls |F'(x0)| > 1: abstossender Fixpunkt")
