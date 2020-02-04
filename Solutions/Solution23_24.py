def write_string_to_file(input_text, filename='sol23_output.txt'):
    """
    Schreibt einen gegebenen String in die Datei (überschreibt vorherigen Inhalt)
    :param input_text: zu schreibender Text
    :param filename: Name der Zieldatei
    :return:
    """
    with open(filename, 'w') as output_file:
        output_file.write(input_text)


def append_string_to_file(input_text, filename='sol23_output.txt'):
    """
    Wie "write_string_to_file", aber der Text wird an den aktuellen Inhalt der Datei angehangen
    """
    with open(filename, 'a') as output_file:
        output_file.write(input_text)


def read_binary_file(filename='sol23_output.txt'):
    """
    Lese die Datei im Binär-Modus
    :param filename: Name der zu lesenden Datei
    :return: Inhalt der Datei
    """

    with open(filename, 'rb') as input_file:
        content = input_file.read()
    return content


if __name__ == '__main__':
    write_string_to_file('Hello World')
    append_string_to_file('ÄÄ')

    binary_contents = read_binary_file()
    decoded_contents = binary_contents.decode('utf-8', 'ignore')

    print('Binär: {}'.format(binary_contents))
    print('String: {}'.format(decoded_contents))