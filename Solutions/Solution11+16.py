def add(a, b):
    """
    Addiert zwei Zqahlen
    :param a: erster Sumand
    :param b: zweiter Sumand
    :return: Summe
    """
    return a + b


def sub(a, b):
    """
       Subtrahiert zwei Zqahlen
       :param a: erster Subtrahend
       :param b: zweiter Subtrahend
       :return: Subtraktion
       """
    return a - b


def select_op():
    # Wir geben an, welche Möglichkeiten zu auswahl stehen.
    # Üblicherweise werden dies nummeriert und über die Nummer gewählt, da hiermit das Parsen erleichtert wird.
    print("Mögliche Funktionen:\n"
          "1: +\n"
          "2: -\n")

    # Die Auswahl wird abgefragt
    op = input("Welche Funktion:")

    # Abhängig von der Auswahl wird die aufzurufende Funktion gesetzt
    if op == "1":
        call = add

    if op == "2":
        call = sub

    # Die Eingabewerte werden abgefragt
    a = int(input("Wie viel ist a:"))
    b = int(input("Wie viel ist b:"))

    # Die Funktion wird aufgerufen und das Ergebnis ausgegeben
    ret = call(a, b)
    print(ret)


if __name__ == '__main__':
    select_op()