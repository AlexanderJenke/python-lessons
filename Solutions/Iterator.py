class Reverse:
    def __init__(self, l: list):
        self.list = l

    def __iter__(self):
        self.i = len(self.list)
        return self

    def __next__(self):
        self.i -= 1
        if self.i < 0:
            raise StopIteration
        return self.list[self.i]


l = "Lorem Ipsum"
it = Reverse(l)
for i in it:
    print(i)
