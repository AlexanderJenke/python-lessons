class Person:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Ich bin {}'.format(self.name))


class Akademiker(Person):

    def __init__(self, name, titel):
        """
        super() referenziert die Klasse (Person) von der die aufrufende Klasse (Akademiker) erbt.
        Man hätte hier auch einfach nur die Zeile "self.name = name" aufrufen können,
        im Allgemeinen ist es aber wichtig, den "Eltern-Constructor" aufzurufen, damit Änderungen an diesem
        auch automatisch das Verhalten der Kind-Klassen verändert.
        """

        super().__init__(name)
        self.titel = titel

    def greet(self):
        print('Ich bin {} {}'.format(self.titel, self.name))


if __name__ == '__main__':
    bob = Person('Bob')
    alice = Akademiker('Alice', 'Prof.')

    bob.greet()
    alice.greet()
