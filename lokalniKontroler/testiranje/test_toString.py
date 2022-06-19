import unittest
import sys 
import os
sys.path.insert(0, "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler")
from cuvanjeKontrolera import toString


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        ulaz = 1
        ocekujemo = toString(ulaz)
        self.assertEqual(ocekujemo, "1")
    def test_case2(self):
        ulaz = 2005
        ocekujemo = toString(ulaz)
        self.assertEqual(ocekujemo, "2005")

if __name__ == '__main__':
    unittest.main()