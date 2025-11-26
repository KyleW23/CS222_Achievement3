import unittest
from romanNumeral import RomanNumeral

class TestRomanNumeral(unittest.TestCase):
    def setUp(self):
        self.r = RomanNumeral()
        
    def test_toRoman(self):
        self.assertEqual(self.r.toRoman(1), 'I')
        self.assertEqual(self.r.toRoman(12), 'XII')
        self.assertEqual(self.r.toRoman(149), 'CXLIX')
        self.assertEqual(self.r.toRoman(2841), 'MMDCCCXLI')