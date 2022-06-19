import unittest
import sys 
import os
sys.path.insert(0, "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler")
from lokalniKontroler import toInt


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        ulaz = 1
        ocekujemo = toInt(ulaz)
        self.assertEqual(ocekujemo, ulaz)

    def test_case2(self):
        ulaz = "x"
        ocekujemo = toInt(ulaz)
        self.assertEqual(ocekujemo, "ERROR")

    def test_case3(self):
        ulaz = " "
        ocekujemo = toInt(ulaz)
        self.assertEqual(ocekujemo, "ERROR")


if __name__ == '__main__':
    unittest.main()