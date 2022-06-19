import unittest
import sys 
import os
sys.path.insert(0, "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniUredjaj")
from uredjajFunkcije import konektujNaKontroler

class MyTestCase(unittest.TestCase):
    def test_case1(self):
        ulazPort = 2003
        tipUredjaja = 1
        ocekujemo = konektujNaKontroler(ulazPort,tipUredjaja)
        self.assertEqual(ocekujemo, None )
    
    def test_case2(self):
        ulazPort = "x"
        tipUredjaja = 1
        ocekujemo = konektujNaKontroler(ulazPort,tipUredjaja)
        self.assertEqual(ocekujemo, "ERROR")
    def test_case3(self):
        ulazPort = 2003
        tipUredjaja = 3
        ocekujemo = konektujNaKontroler(ulazPort,tipUredjaja)
        self.assertEqual(ocekujemo,"ERROR" )
    def test_case4(self):
        ulazPort = 2003
        tipUredjaja = "32"
        ocekujemo = konektujNaKontroler(ulazPort,tipUredjaja)
        self.assertEqual(ocekujemo, "ERROR")

if __name__ == '__main__':
    unittest.main()