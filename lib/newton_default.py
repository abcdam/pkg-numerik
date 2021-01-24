import numpy as np
steps = 20
# tol = 0.00001

def function(x):
    return x ** 2 - 2


def derivative(x):
    return 2 * x


def second_derivative(x):
    return 2


def newton_step(x):
    return x - function(x) / derivative(x)


def condition(x):
    return np.abs(function(x) * second_derivative(x) / derivative(x) ** 2) < 1


def newton(start):
    k = 0
    x_current = start
    # np.abs(function(x0)-function(x1))>tol:
    while k < steps:
        x_current = newton_step(x_current)
        k = k + 1
    return x_current

# example

for i in range(-5,5):
    if i == 0:continue
    print(True) if condition(i) else print(False)
    print(newton(i))