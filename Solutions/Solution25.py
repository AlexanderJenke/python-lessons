teiler_von_16 = {1, 2, 4, 8, 16}
teiler_von_18 = {1, 2, 3, 6, 9, 18}

if __name__ == '__main__':
    # Gemeinsame Elemente: durch Schnittmenge
    gemeinsame_teiler = teiler_von_16 & teiler_von_18

    # Nicht gemeinsame Elemente: durch Symmetrische Differenz
    nicht_gemeinsame_teiler = teiler_von_16 ^ teiler_von_18

    # Teilbarkeit: durch Teilmengenbeziehung der Teiler
    teilbar_durch_16 = bool(teiler_von_16 <= teiler_von_18)

    print('Gemeinsame Teiler: {}'.format(gemeinsame_teiler))
    print('Nicht gemeinsame Teiler: {}'.format(nicht_gemeinsame_teiler))
    print('18 ist durch 16 teilbar: {}'.format(teilbar_durch_16))
