#!/usr/bin/env python

"""
    A simple Vigenere cipher implementation.
"""
from __future__ import unicode_literals

from operator import add, sub

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def shift_text(text, key='LEMON', encrypt=True):
    """Apply the Vigenere algorithm to text.

    We make use of the operator module to provide the same interface to
    both encryption and decryption, this way we don't violate DRY!

    Args:
        text: The text to encode
        shift: An integer amount to rotate our string by
        encrypt: Which direction are we moving?
    """
    # Try to match our alphabet more closely
    text = text.upper()
    key = key.upper()

    operator = add if encrypt else sub
    result = ''
    for index, char in enumerate(text):
        key_index = index % len(key)
        key_char = key[key_index]
        try:
            new_index = operator(alphabet.index(char), alphabet.index(key_char)) % 26
            new_character = alphabet[new_index]
        except ValueError:
            # Character was not in our alphabet, just use the same one!
            new_character = char

        result += new_character
    return result


def encrypt(cleartext, key='LEMON'):
    """Encrypt a clear text.

    Args:
        ciphertext: The encrypted cleartext
        shift: An integer amount to rotate our string by
    """
    return shift_text(cleartext, key, True)


def decrypt(ciphertext, key='LEMON'):
    """Decrypt a cipher text.

    Args:
        ciphertext: The encrypted cleartext
        shift: An integer amount to rotate our string by
    """
    return shift_text(ciphertext, key, False)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print 'Usage: python vigenere_simple.py LEMON "secret message"'
    else:
        key = sys.argv[1]
        message = sys.argv[2]

        is_encrypt = True
        if len(sys.argv) == 4:
            is_encrypt = sys.argv[3] == 'encrypt'

        message = message.replace(' ', '')

        print shift_text(message, key, is_encrypt)
