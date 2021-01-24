import numpy as np

d = True

def solve(A,x0,b,n,eps):
    (L,D,R) = decomposition(A)
    x_i = np.copy(x0)
    x_n = np.zeros((len(A),1))
    D_inv = np.linalg.inv(D)
    LR = L+R
    Di_b = np.matmul(D_inv,b)
    DiLR = np.matmul(-1*D_inv,LR)
    counter = 0
    eps = np.linalg.norm(np.full([len(A),1],eps),np.inf)
    if d:
        print("L=\n{}\nD=\n{}\nR=\n{}\n".format(L,D,R))
    while counter < n:
        for i in range(len(A)):
            for k in range(len(A)):
                if DiLR[i][k] == 0: continue
                if k >= i:
                    x_n[i] = x_n[i] + DiLR[i][k]*x_i[k]
                else:
                    x_n[i] = x_n[i] + DiLR[i][k]*x_n[k]
            x_n[i] = x_n[i] + Di_b[i]
        if d:
            print('x_{}=\n{}'.format(counter+1,x_n))
        if np.linalg.norm(x_i-x_n,np.inf) < eps:
            return x_n
        counter = counter + 1
        x_i = np.copy(x_n)
        x_n[::] = 0
    return x_i

def decomposition(A):
    L = np.tril(A,-1)
    D = np.diagflat(np.diag(A))
    R = np.triu(A,1)
    return (L,D,R)

# example

A = np.array([[8,5,2],[5,9,1],[4,2,7]])
b = np.array([[19],[5],[34]])
x0 = np.array([[1],[-1],[3]], dtype='float64')
n = 1000
solve(A,x0,b,n,1e-17)