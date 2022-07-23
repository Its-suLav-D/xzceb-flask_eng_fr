import unittest

# from machinetranslation.translator import french_to_english, english_to_french
from translator import french_to_english, english_to_french

   
class TestFrenchToEnglish(unittest.TestCase): 
    def test_non_empty(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Hola')

    def test_empty(self):
        self.assertEqual(french_to_english(''),"Text is Empty" )
        self.assertNotEqual(french_to_english(''), " ")

class TesEnglishToFrench(unittest.TestCase):
    def test_non_empty(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hola')
    
    def test_empty(self):
        self.assertNotEqual(english_to_french(''), " ")
        self.assertEqual(english_to_french(''),"Text is Empty")


unittest.main()