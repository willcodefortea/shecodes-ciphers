#!/usr/bin/env python

"""
    A broken Caeser cipher implementation.

    There are 5 bugs in the code below, can you fix them?

    Once they're fixed, this script should run without erroring. Once that's
    complete, can you crack the encrypted text at the bottom of this file?
"""
from __future__ import unicode_literals

alphabet = 'ABCDFEGHIJKLMNQPORSTUVWXYZ'


def shift_text(text, shift=13):
    """Rotate each character in `text` by `shift` amount.

    Args:
        text: The text to shift
        shift: An integer amount to rotate our string by
    """
    result = ''

    for character in text.upper():
        try:
            new_character_index = (alphabet.index(character) - shift) % 13
            new_character = alphabet[new_character_index]
        except ValueError:
            # Character was not in our alphabet, just use the same one!
            new_character = character

        result += new_character
    return result


def encrypt(cleartext, shift=13):
    """Decrypt a cipher text.

    Args:
        ciphertext: The encrypted cleartext
        shift: An integer amount to rotate our string by
    """
    return shift_text(text=cleartext, shift=shift)


def decrypt(ciphertext, shift=13):
    """Decrypt a cipher text.

    Args:
        ciphertext: The encrypted cleartext
        shift: An integer amount to rotate our string by
    """
    return shift_text(text=ciphertext, shift=shift)


def main():
    cleartext = 'The quick brown fox jumps over the lazy dog'
    shift = 4
    ciphertext = encrypt(cleartext, shift)

    assert ciphertext == 'XLI UYMGO FVSAR JSB NYQTW SZIV XLI PEDC HSK', 'Incorrect encryption.'

    decrypted = decrypt(cleartext, shift)
    assert decrypted == 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 'Incorrect decryption.'

    encrypted = "YMDXQK IME PQMP: FA NQSUZ IUFT. FTQDQ UE ZA PAGNF ITMFQHQD MNAGF FTMF. FTQ DQSUEFQD AR TUE NGDUMX IME EUSZQP NK FTQ OXQDSKYMZ, FTQ OXQDW, FTQ GZPQDFMWQD, MZP FTQ OTUQR YAGDZQD. EODAASQ EUSZQP UF. MZP EODAASQ'E ZMYQ IME SAAP GBAZ 'OTMZSQ, RAD MZKFTUZS TQ OTAEQ FA BGF TUE TMZP FA. AXP YMDXQK IME ME PQMP ME M PAAD-ZMUX.\n\nYUZP! U PAZ'F YQMZ FA EMK FTMF U WZAI, AR YK AIZ WZAIXQPSQ, ITMF FTQDQ UE BMDFUOGXMDXK PQMP MNAGF M PAAD-ZMUX. U YUSTF TMHQ NQQZ UZOXUZQP, YKEQXR, FA DQSMDP M OARRUZ-ZMUX ME FTQ PQMPQEF BUQOQ AR UDAZYAZSQDK UZ FTQ FDMPQ. NGF FTQ IUEPAY AR AGD MZOQEFADE UE UZ FTQ EUYUXQ; MZP YK GZTMXXAIQP TMZPE ETMXX ZAF PUEFGDN UF, AD FTQ OAGZFDK'E PAZQ RAD. KAG IUXX FTQDQRADQ BQDYUF YQ FA DQBQMF, QYBTMFUOMXXK, FTMF YMDXQK IME ME PQMP ME M PAAD-ZMUX.\n\nEODAASQ WZQI TQ IME PQMP? AR OAGDEQ TQ PUP. TAI OAGXP UF NQ AFTQDIUEQ? EODAASQ MZP TQ IQDQ BMDFZQDE RAD U PAZ'F WZAI TAI YMZK KQMDE. EODAASQ IME TUE EAXQ QJQOGFAD, TUE EAXQ MPYUZUEFDMFAD, TUE EAXQ MEEUSZ, TUE EAXQ DQEUPGMDK XQSMFQQ, TUE EAXQ RDUQZP, MZP EAXQ YAGDZQD. MZP QHQZ EODAASQ IME ZAF EA PDQMPRGXXK OGF GB NK FTQ EMP QHQZF, NGF FTMF TQ IME MZ QJOQXXQZF YMZ AR NGEUZQEE AZ FTQ HQDK PMK AR FTQ RGZQDMX, MZP EAXQYZUEQP UF IUFT MZ GZPAGNFQP NMDSMUZ.\n\nFTQ YQZFUAZ AR YMDXQK'E RGZQDMX NDUZSE YQ NMOW FA FTQ BAUZF U EFMDFQP RDAY. FTQDQ UE ZA PAGNF FTMF YMDXQK IME PQMP. FTUE YGEF NQ PUEFUZOFXK GZPQDEFAAP, AD ZAFTUZS IAZPQDRGX OMZ OAYQ AR FTQ EFADK U MY SAUZS FA DQXMFQ. UR IQ IQDQ ZAF BQDRQOFXK OAZHUZOQP FTMF TMYXQF'E RMFTQD PUQP NQRADQ FTQ BXMK NQSMZ, FTQDQ IAGXP NQ ZAFTUZS YADQ DQYMDWMNXQ UZ TUE FMWUZS M EFDAXX MF ZUSTF, UZ MZ QMEFQDXK IUZP, GBAZ TUE AIZ DMYBMDFE, FTMZ FTQDQ IAGXP NQ UZ MZK AFTQD YUPPXQ-MSQP SQZFXQYMZ DMETXK FGDZUZS AGF MRFQD PMDW UZ M NDQQLK EBAF -- EMK EMUZF BMGX'E OTGDOTKMDP RAD UZEFMZOQ -- XUFQDMXXK FA MEFAZUET TUE EAZ'E IQMW YUZP.\n\nEODAASQ ZQHQD BMUZFQP AGF AXP YMDXQK'E ZMYQ. FTQDQ UF EFAAP, KQMDE MRFQDIMDPE, MNAHQ FTQ IMDQ-TAGEQ PAAD: EODAASQ MZP YMDXQK. FTQ RUDY IME WZAIZ ME EODAASQ MZP YMDXQK. EAYQFUYQE BQABXQ ZQI FA FTQ NGEUZQEE OMXXQP EODAASQ EODAASQ, MZP EAYQFUYQE YMDXQK, NGF TQ MZEIQDQP FA NAFT ZMYQE. UF IME MXX FTQ EMYQ FA TUY.\n\nAT! NGF TQ IME M FUSTF-RUEFQP TMZP MF FTQ SDUZPEFAZQ, EODAASQ! M ECGQQLUZS, IDQZOTUZS, SDMEBUZS, EODMBUZS, OXGFOTUZS, OAHQFAGE AXP EUZZQD! TMDP MZP ETMDB ME RXUZF, RDAY ITUOT ZA EFQQX TMP QHQD EFDGOW AGF SQZQDAGE RUDQ; EQODQF, MZP EQXR-OAZFMUZQP, MZP EAXUFMDK ME MZ AKEFQD. FTQ OAXP IUFTUZ TUY RDALQ TUE AXP RQMFGDQE, ZUBBQP TUE BAUZFQP ZAEQ, ETDUHQXXQP TUE OTQQW, EFURRQZQP TUE SMUF; YMPQ TUE QKQE DQP, TUE FTUZ XUBE NXGQ; MZP EBAWQ AGF ETDQIPXK UZ TUE SDMFUZS HAUOQ. M RDAEFK DUYQ IME AZ TUE TQMP, MZP AZ TUE QKQNDAIE, MZP TUE IUDK OTUZ. TQ OMDDUQP TUE AIZ XAI FQYBQDMFGDQ MXIMKE MNAGF IUFT TUY; TQ UOQP TUE ARRUOQ UZ FTQ PAS-PMKE; MZP PUPZ'F FTMI UF AZQ PQSDQQ MF OTDUEFYME.\n"

    print ('Encrypted:\n\n%s\n\n' % encrypted)
    shift = 0
    print ('Decrypted:\n\n%s\n\n' % decrypt(encrypted, shift))

if __name__ == '__main__':
    main()
