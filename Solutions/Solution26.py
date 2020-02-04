import os


def list_all_folders(path='..'):
    """
    Gibt alle Ordnernamen im gegebenen Verzeichnis
    default-Wert '..' bedeutet ein Ordner nach "oben" von dem Ort aus, wo dieses Skript aufgerufen wird.
    """
    folders = []

    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            folders.append(entry)

    return folders


if __name__ == '__main__':
    print(list_all_folders())
