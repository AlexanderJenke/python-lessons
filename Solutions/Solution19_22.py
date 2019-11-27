import string

# Task 19 - 21
ALPHABET = string.ascii_lowercase + string.punctuation + ' '


def prepare(text):
    lower_text = text.lower()

    lines = lower_text.splitlines()

    return lines


def substitute(text, offset=0):
    result = ''
    alphabet = ALPHABET

    for char in text:
        index = alphabet.find(char)

        if index == -1:
            print('Unbekanntes Zeichen:', ord(char))
            continue

        new_index = (index + offset) % len(alphabet)
        result += alphabet[new_index]

    return result


def substitute_1(text, offset=0):
    alphabet = ALPHABET
    mapping = dict()

    for char in alphabet:
        index = alphabet.find(char)
        new_index = (index + offset) % len(alphabet)
        mapping[ord(char)] = ord(alphabet[new_index])

    return text.translate(mapping)


def analize(text, most_used=' '):
    counts = []

    for letter in set(text):
        if letter != ' ':
            counts.append((text.count(letter), letter))

    counts.sort()
    count, most_used_letter = counts[-1]

    guessed_key = (ALPHABET.index(most_used_letter) - ALPHABET.index(most_used)) % len(ALPHABET)
    print('I guess the key is {key}, {letter} occured {nr} times'.format(letter=most_used_letter, key=guessed_key,
                                                                         nr=count))


def caesar_encrypt(text, offset):
    lines = prepare(text)
    encrypted_lines = []

    for line in lines:
        encrypted_lines.append(substitute(line, offset))

    ciphertext = '\n'.join(encrypted_lines)
    return ciphertext


def caesar_decrypt(text, offset):
    return caesar_encrypt(text, len(ALPHABET) - offset)


if __name__ == '__main__':
    pt = """Welcome to the Faculty of Computer Science
Six decades of research and teaching experience and the international orientation
characterize the largest educational institution of computer science of Saxony. The faculty
covers the entire spectrum of computer science and provides a research-oriented and practical education in twelve courses at high standards. The research aims to develop new technologies for the future: The Internet of Services, Cloud Computing, Data Security, BigData and Interactive Visual Computing are examples of many research fields that give new impulses to the teaching. "Silicon Saxony" also leads the software research to a new dimension.
"""
    key = 13

    ct = caesar_encrypt(pt, key)
    decr = caesar_decrypt(ct, key)
    print('Ciphertext:\n' + ct)
    print('Decryption:\n' + decr)
    print('Analyse:')
    analize(ct)

    # Wenn alles funktioniert hat:
    print("War alles richtig?", '\n'.join(pt.splitlines()).lower() == decr)
