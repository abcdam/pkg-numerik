import numpy as np
limit = 10

def function(x):
    return x**2-2
def sek_step(x1,x2):
    return x2-(x2-x1)/(function(x2)-function(x1))*function(x2)
def sekantenverfahren(x0, x1, tol):
    k = 0
    while np.abs(function(x0)-function(x1))>tol:
        x0 = sek_step(x0,x1)
        print(x0)
        (x0, x1) = (x1, x0)
        k = k+1
    return x1

# example

print(sekantenverfahren(-2,-1,1e-20))