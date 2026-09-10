# E)

import unittest

from p5_Marrero_Jose import( caesar_cipher , caesar_decipher, letter_frequency )

class TestCaesarCipher(unittest.TestCase):
    def test_basic_encryption(self):
        result = caesar_cipher("abc", 3)
        self.assertEqual(result, "def")

    def test_preserves_non_alpha(self):
        result = caesar_cipher("abc! 123", 3)
        self.assertEqual(result, "def! 123")

    def test_wrap_around_alphabet(self):
        result = caesar_cipher("xyz", 3)
        self.assertEqual(result, "abc")    

    def test_decipher(self):
        result = caesar_decipher("def", 3)
        self.assertEqual(result, "abc")    

    def test_frequency_ignores_non_letters(self):
        result = letter_frequency("1234!?")
        self.assertEqual(sum(result.values()), 0)

if __name__ == "__main__":
    unittest.main()        