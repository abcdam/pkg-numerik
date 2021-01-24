# Skript S. 19 - 21, S. 25
import numpy as np

exakter_Wert = 0.739
gerundeter_Wert = 0.740
abgeschnittener_Wert = 0.730
# Anzahl Stellen, die dargestellt werden können und auf die damit gerundet bzw. gekürzt wird.
stellen_Mantisse = 2
# Bei 0.71: exakter Wert 0.71, Stellen Exponenten: 0; bei 7.1: exakter Wert 0.71, Stellen Exponenten: 1
stellen_Exponent = 0
basis = 10 # Beliebige gerade Basis

# Beliebige gerade Basis
# Halb so gross wie beim Abschneiden:
max_absoluter_Fehler_beliebige_gerade_Basis_runden = (basis / 2) * basis**(stellen_Exponent-stellen_Mantisse-1)
print('Maximaler absoluter Fehler für die gerade Basis', basis, 'mit Runden = ', max_absoluter_Fehler_beliebige_gerade_Basis_runden)
# Doppelt so gross wie beim Runden:
max_absoluter_Fehler_beliebige_gerade_Basis_abschneiden = basis**(stellen_Exponent-stellen_Mantisse)
print('Maximaler absoluter Fehler für die gerade Basis', basis, ' mit Abschneiden = ', max_absoluter_Fehler_beliebige_gerade_Basis_abschneiden)

absoluter_Fehler_beliebige_gerade_Basis_runden = abs(gerundeter_Wert-exakter_Wert)
print('Absoluter Fehler für die gerade Basis', basis, 'mit Runden = ', absoluter_Fehler_beliebige_gerade_Basis_runden)

absoluter_Fehler_beliebige_gerade_Basis_abschneiden = abs(abgeschnittener_Wert-exakter_Wert)
print('Absoluter Fehler für die gerade Basis', basis, 'mit Abschneiden = ', absoluter_Fehler_beliebige_gerade_Basis_abschneiden)

print('Der gerundetet absolute Fehler ist kleiner als der maximale absolute Fehler.')
print('Der absolute Fehler beim Abschneiden kann fast doppelt so gross sein, wie beim Runden.')
print('Bei ungeraden Basen gilt dies nicht. Entweder müssten die Abschätzungen oder die Rundungsregeln'
      'angepasst werden.')


print('***Berechne den Nährungswert')
max_absoluter_Fehler = 0.001
exakter_Wert = np.sqrt(2)
# Berechne den Exponeten für den absoluten Fehler
exponent = abs(np.log10(np.abs(max_absoluter_Fehler)).astype(int))
naehrung = np.round(exakter_Wert, exponent)
absolute_Fehler  = exakter_Wert - np.round(exakter_Wert, exponent)
print('Der exakte Wert beträgt:', exakter_Wert)
print('Der Naehrungwert beträgt:', naehrung)
print('Der absolute Fehler beträgt', absolute_Fehler, '<  maximale absolute Fehler', max_absoluter_Fehler)

