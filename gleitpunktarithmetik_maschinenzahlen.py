# Gleitpunktarithmetik und Maschinengenauigkeit

'''
Beispiel:   Bestimmen Sie die Anzahl verschiedener Maschinenzahlen auf
            einem Rechner, der [15]-stellige Gleitpunktzahlen mit [5]-stelligen
            Exponenten sowie dazugehörige Vorzeichen im Dualsystem verwendet.

Lösung:     machine_numbers(15,5)
        =>  2064384 2064385
'''


def machine_numbers(digits_float, digits_power, system=2, verbose=False):
    # die erste Nachkommaziffer muss 1 sein, mit dem Vorzeichen gleicht sich das wieder aus
    possibilities = (system ** digits_float)
    # fuer den Exponenten gibt es 2^digits_power moeglichkeiten,
    # mit vorzeichen 2^(digits_power+1) - 1 weil die Null doppelt gezählt wird.
    possibilities_power = (system ** (digits_power + 1)) - 1
    possibilities_total = possibilities * possibilities_power

    if verbose:
        print("Anzahl Möglichkeiten insgesamt (ohne Null): ", possibilities_total, "Mit Null: ",
              possibilities_total + 1)
    else:
        print(possibilities_total, possibilities_total + 1)


machine_numbers(15, 5)
