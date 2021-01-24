import scipy.linalg
import numpy as np

x = np.array([-1, 2, 3])

print('Vektor x Normen')
print('1-Norm, Summennorm:', scipy.linalg.norm(x, 1))
print('2-Norm, Euklidische Norm:', scipy.linalg.norm(x,2), '= Wurzel(', scipy.linalg.norm(x)**2, ')')
print('Unentlich-Norm, Maximumnorm:', scipy.linalg.norm(x, np.inf))

A = np.array([[0.00001, 0.00001], [2, 3]])

print()
print('Matrix A Normen')
print('1-Norm, Spaltensummennorm:', scipy.linalg.norm(A, 1))
# 2-Norm, Spektralnorm = Wurzel(grösster Eigenwert von (AT x A))
ew, ev = scipy.linalg.eig(np.transpose(A)@A)
ew_abs = np.abs(ew)
ew_max = np.argmax(ew_abs)
spektralnorm = np.sqrt(ew[ew_max])
print('2-Norm, Spektralnorm:', spektralnorm)
print('Unentlich-Norm, Zeilensummennorm:', scipy.linalg.norm(A, np.inf))

print()
print('Konditionszahl in der 1-Norm von A')
print('A', A)
print('1-Norm, Spaltensummennorm:', scipy.linalg.norm(A, 1))
print('A_inverse', np.linalg.inv(A))
print('1-Norm, Spaltensummennorm von A_Inverse:', scipy.linalg.norm(np.linalg.inv(A), 1))
Konditionszahl = scipy.linalg.norm(A, 1) * scipy.linalg.norm(np.linalg.inv(A), 1)
print('Konditionszahl in der 1-Norm ||A|| * ||A_inverse||: = ', Konditionszahl)

print()
print('Lösung für x mit einem gestörten b')
print('Gegeben sind A und gestörtes b')
print('Ax = b_gestört -> x_gestört = A_inverse x b_gestört')
b_gestoert = np.array([0.00001, 1])
x_gestoert = np.array(np.linalg.inv(A) @ b_gestoert)
print('x_gestört = ', x_gestoert)

print()
print('Relativer Fehler')
x = np.array([-1, 1])
relativer_Fehler_x_gestoert = scipy.linalg.norm(x_gestoert - x, 1) / scipy.linalg.norm(x, 1)
print('||x_gestört - x|| = ', scipy.linalg.norm(x_gestoert - x, 1))
print('||x|| = ', scipy.linalg.norm(x , 1))
print('Relativer Fehler = (||x_gestört - x||) / ||x||: ', scipy.linalg.norm(x_gestoert - x, 1),
      '/', scipy.linalg.norm(x, 1), '=', relativer_Fehler_x_gestoert)

print()
print('Abschätzung aufgrund der Kondition')
print('Relativer Fehler: (||b_gestört - b||) / ||b||:')
b = np.array([0, 1])
diff = b_gestoert - b
relativer_Fehler_b_gestoert = scipy.linalg.norm(diff, 1) / scipy.linalg.norm(b, 1)
print('||b_gestört - b|| = ', scipy.linalg.norm(diff, 1))
print('||b|| = ', scipy.linalg.norm(b, 1))
print('Abschätzung aufgrund der Kondition = (||b_gestört - b||) / ||b||: ',
      scipy.linalg.norm(diff, 1), '/',
      scipy.linalg.norm(b, 1), '=', relativer_Fehler_b_gestoert)

print()
print('Daraus folgt: Der relative Fehler', relativer_Fehler_x_gestoert, '≤ Konditionszahl',
      Konditionszahl, '* relative Fehler für b_gestört', relativer_Fehler_b_gestoert, '=',
      Konditionszahl * relativer_Fehler_b_gestoert )
print('Die Abschätzung der Konditionszahl ist zikra um den Faktor',
      Konditionszahl * relativer_Fehler_b_gestoert / relativer_Fehler_x_gestoert,
      'mal grösser, als der tatsächliche Fehler (nicht gut).')

