# Skript S. 21 - 25
import sagemath
import sympy
import numpy as np

# 1. Berechne die Ableitung und die Stammfunktion
# Absoluter Fehler
x = sympy.symbols('x')
#Schreibe hier die Funkton von f(x)
f = x**2 * np.e**-x

print("f(x) =", f)
print("Stammfunktion: F(x) =", sympy.integrate(f, x))
print("Ableitung: f'(x) =", sympy.diff(f, x))

# Formuliere die Konditionszahl mit der obigen Ableitung und vereinfache sie
# K = |f'(x) * |x| / |f(x)|
# K_nicht_vereinfacht = SCHREIBE HIER DIE BERECHNUNG VON K
# Mit '' nur für die Darstellung
K_nicht_vereinfacht = '|(2 * x - x**2)| * |np.e**-x * x| / |(x**2 * np.e**-x)|'
print('K nicht vereinfacht:', K_nicht_vereinfacht)
# Ohne '' nur für die Vereinfachung, *****OHNE abs()
K_vereinfacht = sympy.simplify(2 * x - x**2) * np.e**-x * x / (x**2 * np.e**-x)
print('K vereinfacht:', K_vereinfacht)
# Option für bestimmte x und relative Fehler K, den exakten und den fehlerhaften Wert zu berechnen
print('Option für bestimmte x und relativen Fehler K, den exakten und den fehlerhaften Wert zu berechnen')
x = 5.0
print('x', x)
K = abs((2 * x - x**2)) * abs(np.e**-x * x) / abs((x**2 * np.e**-x))
print('K = ', K)
exakter_Wert = 7*x**5-np.log(x)+3
max_relativer_Fehler_gefordert = 0.05
print('Relativer Fehler', max_relativer_Fehler_gefordert)
fehlerhafte_Wert = exakter_Wert * 1 - max_relativer_Fehler_gefordert
absoluter_Fehler = abs(fehlerhafte_Wert - exakter_Wert)
print('Exakter Wert', exakter_Wert)
print('Fehlerhafte Wert', fehlerhafte_Wert)
print('Absoluter Fehler', absoluter_Fehler, ' = |x_tilde - x|')
print('Relativer Fehler', absoluter_Fehler / abs(x), ' = |x_tilde - x| / |x|')
print('K * Relativer Fehler', K * absoluter_Fehler / abs(x))
print("Falls |f'(x)| > 1 absolute Fehler wird grösser, falls |f'(x)| < 1 absolute Fehler wird kleiner")
# f'(x) = SCHREIBE HIER DIE BERECHNUNG VON f'(x) MIT abs()
print("f'(x) =", abs(-1.0*2.71828182845905**(-x)*x**2 + 2*2.71828182845905**(-x)*x))
# Keine Berechnung nur Darstellung von K und Berechnungsanleitungen
print('Keine Berechnung nur Darstellung von K und Berechnungsanleitungen')
print('K = ', abs(K_vereinfacht))
print('Gleichung nach x auflösen: K * |x_tilde - x| / |x| ≤ relativer Fehler: ', abs(K_vereinfacht), '*', max_relativer_Fehler_gefordert, '≤', max_relativer_Fehler_gefordert)
print('z.B. 1. Fall x - 2 * 0.05 ≤ 0.05 -> x ≤ 3, 2. Fall -(x - 2) * 0.05 ≤ 0.05 -> x ≤ 1')
print('Resultat: Zahl ≤ x ≤ Zahl, z.B. 1 ≤ x ≤ 3')

"""
# Test
# pip install sagemath
import Sage
x,y,z = Sage.var('x,y,z')
f(x,y,z) = x^2 + x*y^2 + y*z^2
f_x = f.diff(x)             # The partial derivative of f(x) w.r.t. x
f_x(1,1,1)                  # Evaluated the partial derivative of f(x) at (1,1,1)
f_i_x = f.integral(x)       # The indefinite integral of f(x) w.r.t x
f_di_x = f.integral(x,0,2)  # The definite integral of f(x) where x
                            # goes from 0 to 2.f_i_x(1,1,1) # Evaluated the integral at (1,1,1)
f_i_x(1,1,1)                # Evaluated the integral at (1,1,1)
"""
