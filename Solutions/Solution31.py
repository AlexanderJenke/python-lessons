class Polynom:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x + self.b * x ** 2 + self.c * x ** 3

    def __str__(self):
        return 'Polynom {}x + {}x² + {}x³'.format(self.a, self.b, self.c)

    def __add__(self, other):
        return Polynom(self.a + other.a, self.b + other.b, self.c + other.c)

    def __sub__(self, other):
        return Polynom(self.a - other.a, self.b - other.b, self.c - other.c)

    def __mul__(self, other):
        return Polynom(self.a * other.a, self.b * other.b, self.c * other.c)


if __name__ == '__main__':
    poly_a = Polynom(a=1, b=3)
    poly_b = Polynom(a=9, c=20)

    poly_c = poly_a + poly_b

    print(poly_a)
    print(poly_b)
    print(poly_c)

    # poly_c.__call__(x) wird hier implizit aufgerufen
    print(poly_c(10))
