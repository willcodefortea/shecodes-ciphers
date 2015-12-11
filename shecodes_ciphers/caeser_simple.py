#!/usr/bin/env python

"""
    A simple Caeser cipher implementation.
"""
from __future__ import unicode_literals

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def shift_text(text, shift=13):
    """Rotate each character in `text` by `shift` amount.

    This is a very basic implementation of a Caeser cipher. We have a few
    limitations / simplifications:

        1.  We only support a reduced alphabet, only upper case ACII characters.
        2.  If we meet a character that is not in our alphabet, we simply reuse
            that character.
        3.  There are better techniques for mapping characters in python using
            `maketrans`.

    Args:
        text: The text to shift
        shift: An integer amount to rotate our string by
    """
    result = ''

    for character in text.upper():
        try:
            new_character_index = (alphabet.index(character) + shift) % 26
            new_character = alphabet[new_character_index]
        except ValueError:
            # Character was not in our alphabet, just use the same one!
            new_character = character

        result += new_character
    return result


def encrypt(cleartext, shift=13):
    """Decrypt a cipher text.

    This is a simple proxy to `shift_text`.

    Args:
        ciphertext: The encrypted cleartext
        shift: An integer amount to rotate our string by
    """
    return shift_text(text=cleartext, shift=shift)


def decrypt(ciphertext, shift=13):
    """Decrypt a cipher text.

    This is a simple proxy to `shift_text`, but with a negative version of the
    shift to move back to our original position.

    Args:
        ciphertext: The encrypted cleartext
        shift: An integer amount to rotate our string by
    """
    return shift_text(text=ciphertext, shift=shift * -1)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print 'Usage: python caeser_simple.py 13 "secret message"'
    else:
        shift = int(sys.argv[1])
        message = sys.argv[2]

        print shift_text(message, shift)
