import unittest
import sys 
import os
sys.path.insert(0, "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\ASM")
from asmFunkcije import BazaPodataka


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        baza = BazaPodataka()
        ocekivano = baza.KonekcijaSaBazom()
        self.assertEqual(ocekivano, "ERROR") #tabele vec postoje



if __name__ == '__main__':
    unittest.main()