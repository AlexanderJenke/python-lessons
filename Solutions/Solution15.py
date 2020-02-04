def solve_poly(x, a=0, b=0, c=0):
    """
    Gibt die Lösung des Polynoms bzw. der Funktion f(x) = ax + bx² + cx³
    :param x:
    :param a: linearer Faktor
    :param b: quadratischer Faktor
    :param c: kubischer Faktor
    :return:
    """
    return a * x + b * x ** 2 + c * x ** 3
