# Fixed Point Iteration Method
# Importing math to use sqrt function
import math
import numpy as np
import sympy as sy


def f(x):
    # return 2 * x - 2 ** x
    return x**3 - x + 0.3


# Re-writing f(x)=0 to x = F(x)
def F(x):
    # return 0.5 * 2 ** x
    return x**3 + 0.3


# Berechne die Ableitung von F(x) zur Kontrolle
def ableitung():
    x = sy.symbols('x')
    f = F(x)
    print('\n\n*** Ableitung von F(x) ***')
    print('Die Ableitung von F(x) lautet', sy.diff(f, x))
    print('Stimmt das mit der Ableitung im Code überein?')
    return


# Calculation F(x)=0 to F_dx(x) (Ableitung von F(x))
def F_dx(x):  # **** MIT abs()
    # return abs(np.log(2) / 2 * 2 ** x)
    return abs(3*x**2)

# Berechne alpha
def alpha(I1, I2):
    alpha = np.max([abs(F_dx(I1)), abs(F_dx(I2))])
    return alpha


# a_priori
def a_priori(I1, I2, x0, e):
    x1 = F(x0)
    alpha_value = alpha(I1, I2)
    max_number_of_Iterations = np.log(e * (1 - alpha_value) / abs(x1 - x0)) / np.log(alpha_value)
    print('\n\n*** A posteriori Fehlerabschätzung ***')
    print('Maximale Anzahl Schritte: n ≥', max_number_of_Iterations)
    print('Es müssen a priori also mindestens', math.ceil(max_number_of_Iterations), 'Schritte durchgeführt werden.')

# a_posteriori
def a_posteriori(e):
    # Werte aus der Fix Point Iteration herauslesen
    xn = 0
    x_n_minus_1 = 0
    number_of_Iterations = 0 # Gewünschte Iteration heraussuchen
    alpha_value = alpha(I1, I2)
    fehler = (alpha_value/(1 - alpha_value)) * abs(xn - x_n_minus_1)
    print('\n\n*** A posteriori Fehlerabschätzung ***')
    print('Vor der Berechnung müssen noch xn und x_n_minus_1 bei der')
    print('gewünschten Anzahl Iterationen aus der Listes der Werte aus der fix point iteration')
    print('herausgelesen und im Code eingeschrieben werden.')
    print('Der Fehler', fehler, ' ist bei der', number_of_Iterations,'. Iteration kleiner als der maximal geforderte Fehler von', e, '.')





# Berechne, ob der Fixpunktsatz von Banach erfüllt ist.
def banach(I1, I2):
    print('\n\n*** Ist der Bachnachsche Fixpunktsatz erfüllt? ***')
    print('Ist die Funktion F(x) monoton steigend oder fallend? Muss ja sein.')
    print('Ist F(', I1, ') =', F(I1), '>', I1, '?')
    print('Ist F(', I2, ') =', F(I2), '<', I2, '?')
    # Berechne alpha
    print('Der Wert von alpha beträgt', alpha(I1, I2))
    print('Alpha muss kleiner als 1 sein.')
    print('Ein kleineres alpha einer Fixpunktgleichungs-Variante, führt zu einer schnelleren Konvergenz.')
    print('Wenn alle obigen Bedingungen erfüllt sind gilt: F : I -> I')
    return


# Implementing Fixed Point Iteration Method
def fixedPointIteration(x0, e, N):
    # Test, ob der Fixpunkt anziehend oder abstossend ist
    print('\n\n*** Fixpunktberechnung ***')
    if F_dx(x0) < 1:
        print('Der Fixpunkt (die mögliche Nullstelle x0) ist anziehend: ', F_dx(x0), '< 1.')
    else:
        print('Der Fixpunkt (die mögliche Nullstelle x0) ist abstossend: ', F_dx(x0), '> 1.')
        print('Es werden darum keine weiteren Berechnungen durchgeführt.')
        exit()
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if step == 1:
            x_Zwischenspeicher = 0
        x1 = F(x0)
        print('Iteration-%d, x1 = %0.15f and f(x1) = %0.15f, Differenz nachfolgender Iterationen: %0.10f' % (step, x1, f(x1), x1 - x_Zwischenspeicher))
        x0 = x1
        x_Zwischenspeicher = x1

        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired x is: %0.15f' % x1)
    else:
        print('\nNot Convergent.')


# Input Section
x0 = input('Mögliche Nullstelle, x0, eingeben: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')
I1 = input('Untere Intervallgrenze: ')
I2 = input('Obere Intervallgrenze: ')

# Converting x0 and e to float
x0 = float(x0)
e = float(e)
I1 = float(I1)
I2 = float(I2)

# Converting N to integer
N = int(N)

# Note: You can combine above three section like this
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))


# Berechne die Ableitung von F(x) zur Kontrolle
ableitung()

# Berechne, ob der Fixpunktsatz von Banach erfüllt ist.
banach(I1, I2)

# a priori Abschätzung
a_priori(I1, I2, x0, e)

# a posteriori Abschätzung
a_posteriori(e)

# Starting Newton Raphson Method
fixedPointIteration(x0, e, N)
