# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from shecodes_ciphers import caeser_simple


class TestCaeserSimple(object):
    def test_encrypt(self):
        cleartext = 'hidden treasure'
        assert caeser_simple.encrypt(cleartext, shift=10) == 'rsnnox dbokcebo'

        cleartext = 'ħiddén tréasuré'
        assert caeser_simple.encrypt(cleartext, shift=10) == 'ħsnnéx dbékcebé'

    def test_decrypt(self):
        cleartext = 'rsnnox dbokcebo'
        assert caeser_simple.decrypt(cleartext, shift=10) == 'hidden treasure'

        cleartext = 'ħsnnéx dbékcebé'
        assert caeser_simple.decrypt(cleartext, shift=10) == 'ħiddén tréasuré'
