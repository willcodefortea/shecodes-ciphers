# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from shecodes_ciphers import caeser_simple


class TestCaeserSimple(object):
    def test_encrypt(self):
        cleartext = 'HIDDEN TREASURE'
        assert caeser_simple.encrypt(cleartext, shift=10) == 'RSNNOX DBOKCEBO'

        cleartext = 'ĦIDDÉN TRÉASURÉ'
        assert caeser_simple.encrypt(cleartext, shift=10) == 'ĦSNNÉX DBÉKCEBÉ'

    def test_decrypt(self):
        cleartext = 'RSNNOX DBOKCEBO'
        assert caeser_simple.decrypt(cleartext, shift=10) == 'HIDDEN TREASURE'

        cleartext = 'ĦSNNÉX DBÉKCEBÉ'
        assert caeser_simple.decrypt(cleartext, shift=10) == 'ĦIDDÉN TRÉASURÉ'
