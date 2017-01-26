def encrypt(text, rot):
    encrypted = ''
    for char in text:
        encrypted = encrypted + rotate_character(char, rot)
    return encrypted

def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_position = alphabet.index(letter)
    return alphabet_position

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if char.isalpha() and char.isupper():
        char = char.lower()
        char = alphabet[(alphabet_position(char) + int(rot)) % 26]
        char = char.upper()
    elif char.isalpha() and char.islower():
        char = alphabet[(alphabet_position(char) + int(rot)) % 26]
    else:
        char = char
    return char
