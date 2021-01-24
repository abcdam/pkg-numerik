import numpy as np

# Für Matrizen, deren Kondition cond(A) gross ist, können sich kleine Fehler im Vektor b (bzw. Rundungs-fehler im
# Verfahren) zu grossen Fehlern im Ergebnis verstärken. Man spricht in diesem Fall von schlecht konditionierten
# Matrizen.


def cond(A):
    cond_1 = np.linalg.norm(A, ord=1) * np.linalg.norm(np.linalg.inv(A), ord=1)
    cond_inf = np.linalg.norm(A, ord=np.inf) * np.linalg.norm(np.linalg.inv(A), ord=np.inf)
    print('Die Kondition per 1-Norm der Matrix lautet: {}'.format(cond_1))
    print('Die Kondition per Unendlichkeits-Norm der Matrix lautet: {}'.format(cond_inf))


def matrix_norm(A):
    print('1-Norm der Matrix: ' + str(np.linalg.norm(A, ord=1)))
    print('Unendlichkeits-Norm der Matrix: ' + str(np.linalg.norm(A, ord=np.inf)))


def vector_norm(v):
    print('1-Norm des Vektors: ' + str(np.sum(np.abs(v))))
    print('2-Norm des Vektors: ' + str(np.linalg.norm(v)))
    n = np.linalg.norm(v, ord=np.inf)
    print('Unendlichkeits-Norm des Vektors: ', n)


# example

#A = np.array([[1,2,3],[3,4,-2],[7,-3,5]])
A = np.array([[240,120,80],[60,180,170],[60,90,500]])
#v = np.array([-1,2,3])
#vector_norm(v)
cond(A)
#matrix_norm(A)
#matrix_norm(np.linalg.inv(A))