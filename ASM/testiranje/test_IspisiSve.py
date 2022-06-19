import unittest
import sys 
import os
sys.path.insert(0, "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\ASM")
from asmFunkcije import BazaPodataka


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        bazaPodataka = BazaPodataka()
        ocekujemo = bazaPodataka.IspisiSve("test")
        self.assertEqual(ocekujemo, "ERROR")

    def test_case2(self):
        bazaPodataka = BazaPodataka()
        ocekujemo = bazaPodataka.IspisiSve(3)
        self.assertEqual(ocekujemo, "ERROR")
    
    def test_case3(self):
        bazaPodataka = BazaPodataka()
        ocekujemo = bazaPodataka.IspisiSve("uredjaji")
        self.assertEqual(ocekujemo, None)



if __name__ == '__main__':
    unittest.main()