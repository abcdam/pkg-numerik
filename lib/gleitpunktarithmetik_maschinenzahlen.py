# Gleitpunktarithmetik und Maschinengenauigkeit

"""
Beispiel:   Bestimmen Sie die Anzahl verschiedener Maschinenzahlen auf
            einem Rechner, der [15]-stellige Gleitpunktzahlen mit [5]-stelligen
            Exponenten sowie dazugehörige Vorzeichen im Dualsystem verwendet.

Lösung:     machine_numbers(15,5)
        =>  2064384 2064385

Beispiel:   Geben Sie die Maschinengenauigkeit einer Rechenmaschine an die mit
            16-stelliger Dezimalarithmetik arbeitet

Lösung:     machine_precision(16,10)
        =>  5 * 10^(-16)
"""


def machine_numbers(digits_float, digits_power, base=2, verbose=False):
    """
    :param digits_float: Stellen Mantisse
    :param digits_power: Stellen Potenz
    :param base: System, für Dualsystem base = 2
    :param verbose: verbose mode
    :return: anzahl möglichkeiten ohne null, anzahl möglichkeiten mit null
    """
    # die erste Nachkommaziffer muss 1 sein, mit dem Vorzeichen gleicht sich das wieder aus
    possibilities = (base ** digits_float)
    # fuer den Exponenten gibt es 2^digits_power moeglichkeiten,
    # mit vorzeichen 2^(digits_power+1) - 1 weil die Null doppelt gezählt wird.
    possibilities_power = (base ** (digits_power + 1)) - 1
    possibilities_total = possibilities * possibilities_power

    if verbose:
        print("Anzahl Möglichkeiten insgesamt (ohne Null): ", possibilities_total, "Mit Null: ",
              possibilities_total + 1)
        return possibilities_total, possibilities_total + 1
    else:
        return possibilities_total, possibilities_total + 1


def machine_precision(digits, base):
    """
    :param digits: Anzahl Stellen
    :param base: System, z.b. für Dezimalarithmetik base = 10
    :return: epsilon, Genauigkeit
    Formel: (base/2) * base ** -digits
    """

    return (base / 2) * (base ** -digits)

# example

print(machine_numbers(15, 5))
print(machine_precision(16, 10))
