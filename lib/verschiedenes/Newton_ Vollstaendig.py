# Skript S. 32 - 34

import numpy as np
import sympy.solvers as sol
import sympy as syp

# Vollständiges Newtonverfahren
def newton(f,Df,x0,epsilon,max_iter):

    """Approximate solution of f(x)=0 by Newton's method.

    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    Df : function
        Derivative (Ableitung) of f(x).
    x0 : number
        Initial guess for a solution f(x)=0.
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of Newton's method.

    Returns
    -------
    xn : number
        Implement the complete Newton's method: compute the linear approximation
        of f(x) at xn and find x intercept by the formula
            x = xn - f(xn)/Df(xn)
        Continue until abs(f(xn)) < epsilon and return xn.
        If Df(xn) == 0, return None. If the number of iterations
        exceeds max_iter, then return None.

    Examples
    --------
    >>> # Stammfunktion
    >>> f = lambda x: np.e ** (x ** 2) + x ** (-3) -10
    >>> # Ableitung
    >>> Df = lambda x: 2 * x * np.e ** (x ** 2) - 3 * x ** (-4)
    >>> # Set Xo
    >>> x0 = 2
    >>> # Set max_Iter
    >>> max_Iter = 20
    >>> # Set maximum error
    >>> error = pow(10, -4)
    >>> newton(f,Df,x0,error,max_Iter)
    """

    print("x 0 =", '{0:.4f}'.format(x0))
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return print('Die Lösung mit dem Newtonverfahren lautet für den Startwert', x0, ':', '{0:.4f}'.format(xn))
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
        print("x", n+1, "=", '{0:.10f}'.format(xn))
    print('Exceeded maximum iterations. No solution found.')
    return None

# Stammfunktion
# f = lambda x: np.e ** (x ** 2) + x ** (-3) - 10
f = lambda x: -5.3933 + 2.5236 * np.e**(2.8681*x)
# Berechne / Überprüfe die Ableitung
x = syp.Symbol('x')
# f_zum_Ableiten = np.e ** (x ** 2) + x ** (-3) - 10
f_zum_Ableiten = -5.3933 + 2.5236 * np.e**(2.8681*x)
print("Die Ableitung f(x) lautet: f'(x) = ", syp.simplify(syp.diff(f_zum_Ableiten, x)))
print('Stimmt die Ableitung mit der Ableitung im Code überein?')
# Ableitung
# Df = lambda x: 2 * x * np.e ** (x ** 2) - 3 * x ** (-4)
Df = lambda x: 7.23793716*2.71828182845905**(2.8681*x)
# Set Xo
x0 = 2.2
# Set maximum error = epsilon
error = pow(10, -4)
# Set max_Iter
max_Iter = 20
newton(f, Df, x0, error, max_Iter)