#!/usr/bin/env python

"""
    A simple Caeser cipher implementation.
"""
from __future__ import unicode_literals

from operator import add, sub

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def shift_text(text, key='LEMON', encrypt=True):
    """Apply the Vigenere algorithm to text, either with addition or subtraction

    Args:
        text: The text to encode
        shift: An integer amount to rotate our string by
        encrypt: Which direction are we moving?
    """
    operator = add if encrypt else sub
    result = ''
    for index, char in enumerate(text):
        key_index = index % len(key)
        key_char = key[key_index]
        new_index = operator(alphabet.index(char), alphabet.index(key_char)) % 26
        new_character = alphabet[new_index]
        result += new_character
    return result



def encrypt(cleartext, key='LEMON'):
    """Decrypt a cipher text.

    This is a simple proxy to `shift_text`.

    Args:
        ciphertext: The encrypted cleartext
        shift: An integer amount to rotate our string by
    """
    return shift_text(cleartext, key, True)


def decrypt(ciphertext, key='LEMON'):
    """Decrypt a cipher text.

    This is a simple proxy to `shift_text`, but with a negative version of the
    shift to move back to our original position.

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

        message = message.replace(' ', '')

        print encrypt(message, key)

