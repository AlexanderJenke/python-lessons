# Vererbung:
# Die Klasse Laptop erbt von Computer, damit kann auch der Laptop die Funktion rechne nutzen
# aber nur der Laptop kann den Akkustand prüfen

class Computer:
    def __init__(self):
        print("new Computer")

    def rechne(self):
        print("... working hard right now!")


class Laptop(Computer):
    def __init__(self):
        super().__init__()
        print("new Laptop")

    def get_akkustand(self):
        print("*Dying Nokia sounds*")


# getattr:
# wenn eine Variable oder Funktion nicht an den üblichen Stellen gefunden wird,
# wird als letzter Versuch die __getattr__ Funktion aufgerufen

class Empty:
    def foo(*args):
        print(F"Die Argumente {args} wurden nicht weiterverarbeitet!")

    def __getattr__(self, item):
        print(F"Die Klasse 'Empty' hat kein Attribut namens {item}!")
        return self.foo


e = Empty()
e.a
e.b()


# Multiple Vererbung
# es kann von mehreren Klassen geerbt werden.
# Python kümmert sich mittels MRO selbstständig darum alle Abhängigkeiten in der richtigen Reihenfolge und nur einmal
# auszuführen

class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        super().__init__()
        print("B")


class C(A):
    def __init__(self):
        super().__init__()
        print("C")


class D(B, C):
    def __init__(self):
        print(D.mro())
        super().__init__()
        print("D")


d = D()


# Funktionsaufruf auf Objekten:
# wird eine Funktion auf einem Objekt aufgerufen wird im endeffekt die Funktion auf der Klasse aufgerufen und das Objekt
# wird als erstes Argument übergeben (deswegen heißt das erste Argument 'self')
#
# F-Strings
# Das print in der bar-Funktion nutzt F-Strings welche erst ab Python >=3.6 verfügbar sind
# hier können variablen in {} geschreiben werden und damit direkt in den String eingesetzt werden
# alternativ kann 'print("bar on {} with var = {}".format(self, self.var)' verwendet werden

class Foo:
    def __init__(self, v):
        """Speichert v als var im Objekt ab"""
        self.var = v

    def bar(self):
        print(F"bar on {self} with var = {self.var}")


foo = Foo(5)
foo2 = Foo(6)

foo2.bar()
foo.bar()
Foo.bar(foo)
