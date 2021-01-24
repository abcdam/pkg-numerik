# Skript S. 32 - 34

import numpy as np
import sympy.solvers as sol
import sympy as syp

# Sekantenverfahren
def sekantenverfahren(f,x0,x1,epsilon,max_iter):

    """Approximate solution of f(x0) - f(x1) = by the Sekanten method.

    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    x0 : number
        First initial guess for a solution f(x0)=0.
    x1 : number
        Second initial guess for a solution f(x1)=0.
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of Newton's method.

    Returns
    -------
    xn : number
        Implement the Sekanten method: compute the linear approximation
        of f(x) at x0 and x1 and find x intercept by the formula
            x = xn - ( xn - xn1 / f(xn) - f(xn1) ) * f(xn(
        Continue until abs(f(xn)) < epsilon and return xn.
        If f(xn) - f(xn1) == 0, return None.
        If the number of iterations exceeds max_iter, then return None.

    Examples
    --------
    >>> # Stammfunktion
    >>> f = lambda x: np.e ** (x ** 2) + x ** (-3) -10
    >>> # Set Xo = Startwert 1
    >>> x0 = -1.0000
    >>> # Set x1 = Startwert 2
    >>> x1 = -1.2000
    >>> # Set max_Iter
    >>> max_Iter = 40
    >>> # Set maximum error
    >>> error = pow(10,-4)
    >>> sekantenverfahren(f,x0,x1,error,max_Iter)
    """

    print("x 0 =", '{0:.4f}'.format(x0))
    xn1 = x0
    xn = x1
    for n in range(0,max_iter):
        fxn1 = f(xn1)
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return print('Die Lösung mit dem Sekantenverfahren lautet für', x0, 'und', x1, ':', '{0:.4f}'.format(xn),'.')
            return round(xn, 4)
        if (fxn - fxn1) == 0:
            print('Devision by zero. No solution found.')
            return None
        temp = xn
        xn = xn - (( xn - xn1) / (fxn - fxn1)) * fxn
        xn1 = temp
        print("x", n+1, "=", '{0:.10f}'.format(temp))
    print('Exceeded maximum iterations. No solution found.')
    return None# Skript S. 32 - 34

# Stammfunktion
f = lambda x: np.e ** (x ** 2) + x ** (-3) - 10
# Set Xo
x0 = 2
# Set Xo
x1 = 2.1
# Set maximum error = epsilon
error = pow(10, -5)
# Set max_Iter
max_Iter = 100
sekantenverfahren(f,x0,x1,error,max_Iter)