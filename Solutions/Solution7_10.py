# Task 7 - 10


# ask name fragt nach deinem Namen und begrüßt dich anschließend.
def askname():
    print("Wie heißt du")
    var = input()  # die Frage nach dem Name könnte auch an die input-Funktion übergeben werden
    print("Hallo " + var + ", willkommen in Python.")


# main-boilerplate:
# aksname() wird nur ausgeführt, wenn das Skript direkt aufgerufen wird.
if __name__ == '__main__':
    askname()
