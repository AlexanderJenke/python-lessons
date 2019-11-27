def fib_rec(n: int):
    """
    Die Fibonacci Reihe wird rekursiv berechnet.
    Hierbei wird für jede zu berechnende Zahl die Funktion erneut aufgerufen,
    bis die Abbruchbedingung (n == 0 or n == 1) erfüllt ist.
    Dadurch ist diese Lösung langsamer und kann nur begrenzt hohe Zahlen n berechnen, da die maximal erlaubte Threadzahl
    erreicht werden kann.

    :param n: zu berechnende Fibonacci-Zahl
    :return: berechnete Fibonacci-Zahl
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n > 1:
        return fib_rec(n - 2) + fib_rec(n - 1)


def fib_itt(n: int):
    """
    Die Fibonacci Reihe wird itterativ berechnet.
    :param n: zu berechnende Fibonacci-Zahl
    :return: Nichts, die Ergebnisse werden zur Laufzeit direkt ausgegeben
    """
    a = 0
    b = 1
    for i in range(n + 1):
        print(a)
        a, b = b, a + b


if __name__ == '__main__':
    # Abfrage der gewünschten Zahl und Aufruf beider Lösungsansätze
    i = int(input("Welche Fibonaccizahl?"))
    print(fib_rec(i))
    fib_itt(i)
