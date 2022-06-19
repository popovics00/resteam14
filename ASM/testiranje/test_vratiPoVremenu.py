import unittest
import sys 
import os
sys.path.insert(0, "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\ASM")
from asmFunkcije import BazaPodataka


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        baza = BazaPodataka()
        ocekivano = baza.VratiPoVremenu("352","10/10/2020","2")
        self.assertEqual(ocekivano, "ERROR")

    def test_case2(self):
        baza = BazaPodataka()
        ocekivano = baza.VratiPoVremenu("10/10/2020","10/10/2021","2")
        self.assertEqual(ocekivano, None)
    
    def test_case3(self):
        baza = BazaPodataka()
        ocekivano = baza.VratiPoVremenu("10/10/2020","32","2")
        self.assertEqual(ocekivano, "ERROR")




if __name__ == '__main__':
    unittest.main()