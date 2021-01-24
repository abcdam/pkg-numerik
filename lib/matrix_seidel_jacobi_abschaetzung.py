import numpy as np


def solve(A):
    L = np.tril(A, -1)
    D = np.diagflat(np.diag(A))
    R = np.triu(A, 1)

    # jacobi
    B_1 = -1 * np.matmul(np.linalg.inv(D), L + R)
    # Gauss Seidel
    B_2 = np.matmul(-1 * np.linalg.inv(D + L), R)

    return B_1, B_2


def a_priori(B, x0, x1, eps):
    x1x0_norm = np.linalg.norm(x1 - x0, np.inf)
    B_norm = np.linalg.norm(B, np.inf)
    return np.log(eps / x1x0_norm * (1 - B_norm)) / np.log(B_norm)


def a_posteriori(B, x_current, x_previous):
    B_norm = np.linalg.norm(B, np.inf)
    # print(B_norm)
    xcxp_norm = np.linalg.norm(x_current - x_previous, np.inf)
    return B_norm * xcxp_norm / (1 - B_norm)

    # Jacobi & Gauss Seidel konvergiert wenn True


def is_diagonally_dominant(A):
    D = np.diag(np.abs(A))
    LR = np.sum(np.abs(A), axis=1) - D
    if np.all(D > LR): return True
    return False

# example

#A = np.array([[8,5,2],[5,9,1],[4,2,7]])
#is_diagonally_dominant(A)
A = np.array([[8,5,2],[5,9,1],[4,2,7]])
x3 = np.array([[ 2.01471266],
 [-1.00535498],
 [ 3.99312276]])
x2 = np.array([[ 2.05109127],
 [-1.01339286],
 [ 3.97463152]])
print(a_posteriori(solve(A)[0],x3,x2))

x0=np.array([[1],[-1],[3]])
x1=np.array([[ 2.25      ],
 [-1.02777778],
 [ 3.86507937]])
print(a_priori(solve(A)[0],x0,x1,1e-4))
print(a_priori(solve(A)[0],x2,x3,1e-4))
