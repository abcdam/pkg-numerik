import numpy as np
import matplotlib.pyplot as plt


# condition is calculated with the following formula:
#
#      |f'(x)|*|x|
# K := -------------
#         |f(x)|
#
# condition K is small -> well conditioned problem
# condition K is big   -> badly conditioned problem
#

def function(x):
    return x * np.exp(x)


def derivative(x):
    return x * np.exp(x) + np.exp(x)


def condition(value):
    return (np.abs(derivative(value)) * np.abs(value)) / np.abs(function(value))


# plot

step = 0.00001
a = -2
b = 2
plotting_range = (a, b + step)
x_values = np.arange(plotting_range[0], plotting_range[1], step)
y_values = [condition(x) for x in x_values]
plt.plot(x_values, y_values, label='K in relation to x')
plt.xlabel('x values')
plt.ylabel('Condition K')
plt.legend()
plt.show()  # not needed in jupyter

"""
Gut konditioniertes Problem fuer K <= 1        

Forderung: |x+1| <= 1    

Fuer x > -1: 
  Forderung: 1 + x <= 1 
    => x <= 0                                  2P
Fuer x < -1:
  Forderung: -(1+x) <= 1
    => -1-x <= 1
    => -x <= 2
    => x >= -2                                 2P
    
Gute Konditionierung fuer -2 <= x <= 0         1P

"""