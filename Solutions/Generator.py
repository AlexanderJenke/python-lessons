class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < 2:
            self.i += 1
            return self.i - 1

        self.a, self.b = self.b, self.a + self.b

        return self.b

def fibonacci():
    a, b = 0, 1
    i = 0
    while True:
        if i < 2:
            i += 1
            yield i - 1
        a, b = b, a + b
        yield b


for i, f1, f2 in zip(range(100), fibonacci(), Fibonacci()):
    print(f"{i}: Fn {f1}, Cls {f2}")
