"""Größter gemeinsamer Teiler mit reduce.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu04/aufgaben/reduce2
"""

from functools import reduce


# Der Algorithmus von Euklid ist etwas zu lange um ihn nur als Lambda-Funktion zu schreiben.
# Deshalb schreiben wir eine Funktion, die den Algorithmus implementiert.
def euklid(a, b):
    """
    Berechnet den größten gemeinsamen Teiler von a und b.
    Args:
    - a (int): Eine Zahl.
    - b (int): Eine Zahl.
    Returns:
    - int: Der größte gemeinsame Teiler von a und b.
    """
    return 0


def gcd(numbers):
    """
    Berechnet den größten gemeinsamen Teiler einer Liste von Zahlen.
    Benutzt dazu die Funktion euklid(a, b) mit reduce().
    Args:
    - numbers (list): Eine Liste von Zahlen.
    Returns:
    - int: Der größte gemeinsame Teiler der Liste.
    """
    return 0


if __name__ == '__main__':
    demo_numbers = [12, 15, 21]
    result = gcd(demo_numbers)
    print(result)  # Sollte 3 ausgeben
