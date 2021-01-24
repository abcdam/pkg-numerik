"""
Anzahl Maschinenzahlen:
m = Mantissenstellen
e = Exponentenstellen
b = Basiszahl
v_mantisse = Vorzeichen mantisse
v_exponent = Vorzeichen exponent
"""

m = 15
e = 5
b = 2
v_mantisse = True
v_exponent = True

mantisse_kombos = b**m
normiert = mantisse_kombos-mantisse_kombos*(1/b)
if v_mantisse:
    normiert = normiert*2
if v_exponent:
    exponent_kombos = (b**(e+1))-1
else:
    exponent_kombos = b^e
result = (normiert * exponent_kombos)+1
print('machine number amount: {}'.format(result))

"""
Maschinengenauigkeit  
n = mantisse stellen  
b = basis
"""

n = 16
b = 10
eps = (b/2)*b**(-n)
print('machine precision eps: {}'.format(eps))