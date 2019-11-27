def sum_all(*args):
    """
    Diese Funktion nimmt eine beliebige Anzahl von Argumenten und summiert diese zusammen.
    :param args: beliebige Anzahl an Summanden
    :return: Summe über alle Argumente
    """
    res = 0  # Ergebnis initialisieren
    for arg in args:  # Schleife über alle Argumente
        res += arg  # Addiert das aktuell betrachtete Argument zum Endergebnis hinzu

    return res  # Endergebnis zurückgeben


if __name__ == '__main__':
    print(sum_all(1, 2, 3, 4))

