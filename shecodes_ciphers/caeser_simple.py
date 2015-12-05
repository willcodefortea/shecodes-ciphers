#!/usr/bin/env python

"""
    A simple Caeser cipher implementation.
"""
from __future__ import unicode_literals

alphabet = 'abcdefghijklmnopqrstuvwxyx'

def encrypt(cleartext, shift=13):
    """Encrypt our cleartext with a shift cipher.

    Args:
        cleartext: A string to encrypt
        shift: An integer amount to rotate our string by
    """

    result = ''

    for character in cleartext:
        # Ensure the character is in our alphabet
        character = character.lower()

        try:
            new_character_index = (alphabet.index(character) + shift) % 26
            new_character = alphabet[new_character_index]
        except ValueError:
            # Character was not in our alphabet, just use the same one!
            new_character = character

        result += new_character
    return result


def decrypt(ciphertext, shift=13):
    """Decrypt a cipher text.

    Args:
        ciphertext: The encrypted cleartext
        shift: An integer amount to rotate our string by
    """
    result = ''

    for character in ciphertext:
        # Ensure the character is in our alphabet
        character = character.lower()

        try:
            new_character_index = (alphabet.index(character) - shift) % 26
            new_character = alphabet[new_character_index]
        except ValueError:
            # Character was not in our alphabet, just use the same one!
            new_character = character

        result += new_character
    return result


def sample(text, shift=13):
    ciphertext = encrypt(text, shift)
    decrypted = decrypt(ciphertext, shift)
    print('Original text', text)
    print('Encrypted', ciphertext)
    print('Decrypted', decrypted)
    assert text == decrypted, 'Invalid decryption'


if __name__ == '__main__':
    # We're running as a script, ask the user what they'd like to do
    from clint.textui import prompt, puts, colored, indent
    from clint.textui.validators import ValidationError

    def option_validator(value):
        if value not in ['1', '2']:
            raise ValidationError('You must choose 1 or 2.')
        return value

    def integer_validator(value):
        try:
            res = int(value)
        except ValueError:
            raise ValidationError('You must provide an integer.')
        return res

    choice = prompt.query(
        'What would you like to do?\n\n'
        '\t1: Encrypt a string\n'
        '\t2: Decrypt a string\n'
        '\n?',
        validators=[option_validator, ]
    )

    value = prompt.query('Input your text:')
    shift = prompt.query('Input your shift:', validators=[integer_validator, ])

    if choice == '1':
        result = encrypt(value, shift)
    else:
        result = decrypt(value, shift)

    puts(colored.green('\nYour result:\n'))
    with indent(4):
        puts(result)
    puts('')
