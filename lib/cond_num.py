from scipy.misc import derivative
import numpy as np

# condition is calculated with the following formula: 
#
#      |f'(x0)|*|x0|
# K := -------------
#         |f(x)|
#
# condition K is small -> well conditioned problem
# condition K is big   -> badly conditioned problem
#
def calculate_cond(function, x0, step=0.1, nth_derivative=1):
    return (np.abs(derivative(function, x0, step, nth_derivative)*np.abs(x0))/np.abs(function(x0))

 