"""
Ax=b
Input:
     (A,b,A_tilde,b_tilde)
output:
     (x,x_tilde,max_possible_relative_error,observed_relative_error, max_possible_abs_error, observed_abs_error)

"""

import numpy as np


def solve(A, A_tilde, b, b_tilde):
    if (not (A.shape[0] == A.shape[1])):
        raise Exception('A is misshaped.')

    if (not (A_tilde.shape[0] == A_tilde.shape[1])):
        raise Exception('Ad is misshaped.')

    if (not (A.shape[0] == b.shape[0])):
        raise Exception('The shape of b does not match the size of A.')

    if (not (A_tilde.shape[0] == b_tilde.shape[0])):
        raise Exception('The shape of bd does not match the size of Ad.')

    x = np.linalg.solve(A, b)

    x_tilde = np.linalg.solve(A_tilde, b_tilde)
    condition = np.linalg.cond(A, np.inf)
    norm_rel_error_A = np.linalg.norm(A - A_tilde, np.inf) / np.linalg.norm(A, np.inf)
    norm_rel_error_b = np.linalg.norm(b - b_tilde, np.inf) / np.linalg.norm(b, np.inf)
    if (condition * norm_rel_error_A < 1):
        dxmax = condition / (1 - (condition * norm_rel_error_A)) * (norm_rel_error_A + norm_rel_error_b)
    else:
        dxmax = np.NaN
    x_max_error = np.linalg.norm(np.linalg.inv(A), np.inf) * np.linalg.norm(b - b_tilde, np.inf)
    x_obs_error = np.linalg.norm(x - x_tilde, np.inf)
    dxobs = np.linalg.norm(x - x_tilde, np.inf) / np.linalg.norm(x, np.inf)

    return x, x_tilde, dxmax, dxobs, x_max_error, x_obs_error

# example

A = np.array([[240,120,80],[60,180,170],[60,90,500]])
b = np.array([[3080],[4070],[5030]])
b_tilde = np.array([[3080*1.05],[4070*1.05],[5030*1.05]])
[x,x_tilde,max_rel_error,obs_rel_error,max_abs_error,obs_abs_error] = solve(A,A,b,b_tilde)
print(max_rel_error)
print(obs_rel_error)
print(max_abs_error)
print(obs_abs_error)
