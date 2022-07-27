import unittest

from translator import french_to_english, english_to_french

class Testf2e(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello') # test translation from Bonjour to Hello
    def test2(self):
        self.assertNotEqual(french_to_english("None"),'') # test null input
    def test3(self):
        self.assertNotEqual(french_to_english(0),0)

class Teste2f(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour') # test translation from Hello to Bonjour
    def test2(self):
        self.assertNotEqual(english_to_french("None"),'') # test null input
    def test3(self):
        self.assertNotEqual(english_to_french(0),0)

unittest.main()