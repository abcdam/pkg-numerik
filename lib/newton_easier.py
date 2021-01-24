steps = 4


def function(x):
    return x ** 2 - 2


def derivative(x):
    return 2 * x


def newton_step(x, x0):
    return x - function(x) / x0


def newton(start):
    k = 0
    x_current = start
    x0 = derivative(start)
    while k < steps:
        x_current = newton_step(x_current, x0)
        k = k + 1
    return x_current


# example

for i in range(-5,5):
    if i == 0:continue
    print(newton(i))
    