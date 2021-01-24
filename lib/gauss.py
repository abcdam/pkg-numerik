import numpy as np

d = False


def solve(A, b):
    if correct_dimensions(A, b):
        return execute_Gauss(A, b)


def correct_dimensions(A, b):
    if len(A.shape) != 2 or len(b.shape) != 2:
        raise Exception("A and b must have only 2 dimensions")
    if b.shape[0] != A.shape[0]:
        raise Exception(
            "{}{}{}{}{}".format("b(", b.size, ") does not have the same amount of elements as A(", A.shape[0],
                                ") has rows"))
    if A.shape[0] != A.shape[1]:
        raise Exception("A is not an nxn Matrix")
    return True


def execute_Gauss(A, b):
    (L, R, p) = decomposition(A)
    y_solution = forward_substitution(L, p, b)
    x_solution = back_substitution(R, y_solution)
    detA = np.linalg.det(A)
    return [L, R, p, x_solution, detA]


def decomposition(A):
    p = np.identity(len(A))
    L = np.identity(len(A))

    for i in range(A.shape[0]):
        if d:
            print("R=\n{}\nL=\n{}\n".format(A, L))
        swap_rows(A, L, i, p)
        for j in range(i + 1, A.shape[0]):
            factor = A[j][i] / A[i][i]
            L[j][i] = factor
            for k in range(A.shape[1]):
                A[j][k] = A[j][k] - factor * A[i][k]
    return (L, A, p)


def forward_substitution(L, p, b):
    Pb = np.matmul(p, b)
    L_temp = np.copy(L)
    solution_vector = []
    for i in range(0, len(L_temp)):
        solution_vector.append(Pb[i][0] / L_temp[i][i])
        for k in range(i + 1, len(L_temp)):
            Pb[k][0] -= L_temp[k][i] * solution_vector[-1]
    return np.transpose(np.array(solution_vector)[np.newaxis])


def back_substitution(A, y_solution):
    solution_vector = []
    for i in range(A.shape[0] - 1, -1, -1):
        solution_vector.insert(0, y_solution[i][0] / A[i][i])
        for k in range(i - 1, -1, -1):
            y_solution[k][0] -= A[k][i] * solution_vector[0]
    return np.array(solution_vector)[np.newaxis]


def swap_rows(A, L, i, p):
    max_v = np.amax(A[i:, i])  # max value in row [i:,i]
    if max_v == 0: raise Exception("Couldn't find a row to use as pivot at " + str(i) + ":" + str(i))
    k = np.where(A[i:, i] == max_v)[0][0] + i  # get index of that value
    A[[i, k]] = A[[k, i]]  # swap row i with row k
    p[[i, k]] = p[[k, i]]
    if i > 0:
        p_temp = np.identity(len(A))
        p_temp[[i, k]] = p_temp[[k, i]]
        if d:
            print("P=\n{}\n--------------".format(p_temp))
        L[:, 0:i] = np.matmul(p_temp, L[:, 0:i])
    elif d:
        print("\n--------------")
    return k

# example

A = np.array([[240,120,80],[60,180,170],[60,90,500]])
b = np.array([[3080],[4070],[5030]])
[L,R,p,x_solution,detA] = solve(A,b)
print(L)
print(R)
print(p)
print(x_solution)
print(detA)