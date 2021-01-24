#Maschinengenauigkeit, EPS
konstante = 2
# Basis der Zahlensysteme B1, B2 etc.
B1 = 2
B2 = 10
# Allgemeine Basis
B = 2
# Stellen der darzustellenden Zahl n1, n2 nach dem Komma etc.
n1 = -46
n2 = -14
# Anzahl Mantissenstellen
n = 5
# Berechne eps1, eps2 etc.
eps1 = (B1 / konstante) * B1**n1
eps2 = (B2 / konstante) * B2**n2
print('EPS 1 = (z.B. x.xxxxe-14 = x.xxxx * 10^-14)', eps1)
print('EPS 2 =', eps2)
print('Folgerung: Weil EPS1 < EPS2 rechnet Maschine 1 genauer.')

print('Maschinengenauigkeit (EPS) bei allgemeiner Basis', B, 'mit', n, 'Mantissenstellen beträgt', B/2* B**-n)
print('Für die kleinste positive Maschinezhal gilt 1 + eps ≠ 1.')
print('Der Rechner kann mit deutlich kleineren Zahlen x < eps noch "genau" rechnen.')
#******Trivia
# Single precision: Zahl 32 Bit davon 1 Bit Vorzeichen, 23 Bit Mantisse, 8 Bit Exponent
# Double precision: Zahl 64 Bit davon 1 Bit Vorzeichen, 52 Bit Mantisse, 11 Bit Exponent
# Anzahl Möglichkeiten um ein Byte zu füllen: 2**8 = 256
# Anzahl Ziffern mit 256 Möglichkeiten im Hexadezimalsystem: 2 Ziffern da FF = 16**2 = 256
# 1 Byte mit 8 Ziffern im Dualsystem braucht im Hexdezimalsystem nur 2 Ziffern.
# Wie viele Stellen braucht man für x1 = 0.00010001, 5 Stellen (10001)
# Alle dualen 3-stelligen postiven Gleitpunktzahlen mit 1-stelligem positiven binären Expomnenten:
# 0.000 x 2**0
# 0.100 x 2^0, ... 0.101, 0.110, 0.111
# 0.100 x 2^1, ... 0.101, 0.110, 0.111, alos 9 Stück
#******Grösste und kleinste Maschinenzahl
# Beispiel: Mantisse 20 Stellen: 2**19 (20-1, da erste Nachkommastelle 1 sein muss).
# Zusammen mit dem Vorzeichen 2**20
# Exponent 4 Stellen: 2**4 zusammen mit dem Vorzeichen 2**5
# Total 2**20 * 2**5 = 2**25 plus 1 =(für die Ziffer 0)
# Grösste Zahl: 0.1111111111111111111 (20 x 1) x 2**1111
# Kleinste Zahl: 0.1 x 2**-1111 dual = 2**-16 dual ungefähr 1.53 x 10**-5
# Beispiel Mantisse n = 4, 0 ≤ e ≤ 3
# xmax = Basis**(maximale Stellen des Exponenten) - Basis**(maximaler Exponent - n)
# z.B 2**(3) - 2**(3-4) = 8 - 0.5 = 7.5 = 0.1111 * 2**3
# xmin = Basis**(minimale Stellen des Exponenten minus 1)
# z.B. 2**(0-1) = 0.5 = 0.1 * 2**0

