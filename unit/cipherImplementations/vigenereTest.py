import unittest
from cipherImplementations.vigenere import Vigenere
import unit.cipherImplementations.cipherTest as cipherTest
import util.textUtils as text_utils


class VigenereTest(unittest.TestCase):
    CipherTest = cipherTest.CipherTest
    cipher = Vigenere(CipherTest.ALPHABET, CipherTest.UNKNOWN_SYMBOL, CipherTest.UNKNOWN_SYMBOL_NUMBER)
    plaintext = b'this is a plaintext with special characters!%%xy<'
    ciphertext_keep_unknown_symbols = b'thit?kv?e?ulaiovhby?witi?usihial?djdvfctesu???ac?'
    ciphertext_remove_unknown_symbols = b'thitkveulaiovhbywitiusihialdjdvfctesuac'
    decrypted_plaintext_keep_unknown_symbols = b'this?is?a?plaintext?with?special?characters???xy?'
    decrypted_plaintext_remove_unknown_symbols = b'thisisaplaintextwithspecialcharactersxy'
    key = text_utils.map_text_into_numberspace(b'aaabcdef', CipherTest.ALPHABET, CipherTest.UNKNOWN_SYMBOL_NUMBER)

    def test1encrypt_keep_unknown_symbols(self):
        plaintext = self.cipher.filter(self.plaintext, keep_unknown_symbols=True)
        plaintext_numbers = text_utils.map_text_into_numberspace(plaintext, self.CipherTest.ALPHABET, self.CipherTest.UNKNOWN_SYMBOL_NUMBER)
        ciphertext_numbers = self.cipher.encrypt(plaintext_numbers, self.key)
        ciphertext = text_utils.map_numbers_into_textspace(ciphertext_numbers, self.CipherTest.ALPHABET, self.CipherTest.UNKNOWN_SYMBOL)
        self.assertEqual(self.ciphertext_keep_unknown_symbols, ciphertext)

    def test2encrypt_remove_unknown_symbols(self):
        plaintext = self.cipher.filter(self.plaintext, keep_unknown_symbols=False)
        plaintext_numbers = text_utils.map_text_into_numberspace(plaintext, self.CipherTest.ALPHABET, self.CipherTest.UNKNOWN_SYMBOL_NUMBER)
        ciphertext_numbers = self.cipher.encrypt(plaintext_numbers, self.key)
        ciphertext = text_utils.map_numbers_into_textspace(ciphertext_numbers, self.CipherTest.ALPHABET, self.CipherTest.UNKNOWN_SYMBOL)
        self.assertEqual(self.ciphertext_remove_unknown_symbols, ciphertext)

    def test3decrypt_keep_unknown_symbols(self):
        ciphertext_numbers = text_utils.map_text_into_numberspace(self.ciphertext_keep_unknown_symbols, self.CipherTest.ALPHABET, self.CipherTest.UNKNOWN_SYMBOL_NUMBER)
        plaintext_numbers = self.cipher.decrypt(ciphertext_numbers, self.key)
        plaintext = text_utils.map_numbers_into_textspace(plaintext_numbers, self.CipherTest.ALPHABET, self.CipherTest.UNKNOWN_SYMBOL)
        self.assertEqual(self.decrypted_plaintext_keep_unknown_symbols, plaintext)

    def test4decrypt_remove_unknown_symbols(self):
        ciphertext_numbers = text_utils.map_text_into_numberspace(self.ciphertext_remove_unknown_symbols, self.CipherTest.ALPHABET, self.CipherTest.UNKNOWN_SYMBOL_NUMBER)
        plaintext_numbers = self.cipher.decrypt(ciphertext_numbers, self.key)
        plaintext = text_utils.map_numbers_into_textspace(plaintext_numbers, self.CipherTest.ALPHABET, self.CipherTest.UNKNOWN_SYMBOL)
        self.assertEqual(self.decrypted_plaintext_remove_unknown_symbols, plaintext)