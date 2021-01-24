import numpy as np

d = False
eps = 1e-14


def solve(A):
    if A.shape[0] != A.shape[1]: raise Exception('A is not an nxn Matrix')
    householders = []
    A_h = A
    for i in range(len(A) - 1):
        e_i = get_unit_v(len(A) - i)
        a_i = np.reshape(A_h[i:, i], (len(A) - i, 1))
        sign = 1 if a_i[0] >= 0 else -1
        v_i = a_i + (sign * np.linalg.norm(a_i)) * e_i
        u_i = 1 / np.linalg.norm(v_i) * v_i
        h_i = np.identity(len(A))
        h_i[i:, i:] = h_i[i:, i:] - 2 * np.matmul(u_i, np.transpose(u_i))
        A_h = np.matmul(h_i, A_h)
        if d:
            print('-----| {} |-----'.format(i))
            print("e_{}=\n{}\na_{}=\n{}\nv_{}=\n{}\nu_{}=\n{}\nh_{}=\n{}\nA_{}=\n{}".format(i, e_i, i, a_i, i, v_i, i,
                                                                                            u_i, i, h_i, i, A_h))
        householders.append(np.transpose(h_i))

    Q = householders[0]
    for i in range(1, len(householders)):
        Q = np.matmul(Q, householders[i])
    A_h[np.abs(A_h) < eps] = 0
    Q[np.abs(Q) < eps] = 0
    return [Q, A_h]


def get_unit_v(length):
    v = np.zeros(length)
    v[0] = 1
    return np.reshape(v, (length, 1))

# example

A = np.array([[1,2,-1],[4,-2,6],[3,1,0]])
solve(A)