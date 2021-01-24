import os
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
import numpy as np


def f_1(x):
    """ f'(x): 1. Ableitung von f(x) """
    return 5 * x ** 4 - 20 * x ** 3 - 90 * x ** 2 + 220 * x + 29


def f(x):
    """ f(x): Gegebene Funktion """
    return x ** 5 - 5 * x ** 4 - 30 * x ** 3 + 110 * x ** 2 + 29 * x - 105


def F(x):
    """ F(x): Stammfunktion von f(x) """
    return 1 / 6 * x ** 6 - x ** 5 - 1 / 4 * 30 * x ** 4 + 1 / 3 * 110 * x ** 3 + 1 / 2 * 29 * x ** 2 - 105 * x


x = np.linspace(-10, 10, 400)
figure, axis = plt.subplots()

axis.plot(x, f(x))
axis.plot(x, f_1(x))
axis.plot(x, F(x))

axis.xaxis.set_major_locator(MultipleLocator(1.0))
axis.xaxis.set_minor_locator(MultipleLocator(0.5))

plt.xlim(-7.5, 7.5)
plt.ylim(-1500, 1500)
plt.grid(True, 'both', 'both')
plt.xlabel("x-Werte")
plt.ylabel("y-Werte")
plt.title("Titel")
plt.legend(["f(x)", "f'(x)", "F(x)"])
plt.show()

# Save to SVG image file using the same file name as this python script
plt.savefig(os.path.splitext(os.path.basename(__file__))[0] + ".svg")

import sympy.plotting as splt
import sympy as sy

x = sy.symbols('x')
# f(x) hier angeben.
f = x ** 5 - 5 * x ** 4 - 30 * x ** 3 + 110 * x ** 2 + 29 * x - 105
p1 = splt.plot(x ** 5 - 5 * x ** 4 - 30 * x ** 3 + 110 * x ** 2 + 29 * x - 105, (x, -7.5, 7.5), show=False, label='f(x)', xlim=[-10,10], ylim=[-1500,1500])
p2 = splt.plot(sy.integrate(f, x), (x, -7.5, 7.5), show=False, label='F(x)', xlim=[-10,10], ylim=[-1500,1500])
p3 = splt.plot(sy.diff(f, x), (x, -7.5, 7.5),show=False,label="f'(x)", xlim=[-10,10], ylim=[-1500,1500])
p1.extend(p2)
p1.extend(p3)

p1[0].line_color='red'
p1[1].line_color='blue'
p1[2].line_color='orange'
p1.legend=True

plt.legend(["f(x)", "f'(x)", "F(x)"])
p1.show()
print("f(x) =", f)
print("Stammfunktion: F(x) =", sy.integrate(f, x))
print("Ableitung: f'(x) =", sy.diff(f, x))
