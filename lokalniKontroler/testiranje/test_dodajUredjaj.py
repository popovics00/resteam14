import unittest
import sys 
import os
sys.path.insert(0, "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler")
from storageFunkije import LocalDeviceStorage
from klasaLokalniUredjaj import Kontroler

class MyTestCase(unittest.TestCase):
    def test_case1(self):
        su = LocalDeviceStorage()
        ocekujemo = su.DodajNoviUredjaj("nesto",2005)
        self.assertEqual(ocekujemo, "ERROR")
    def test_case2(self):
        su = LocalDeviceStorage()
        ocekujemo = su.DodajNoviUredjaj(1,2005)
        self.assertEqual(ocekujemo, "ERROR")
    def test_case3(self):
        su = LocalDeviceStorage()
        ocekujemo = su.DodajNoviUredjaj(Kontroler("kontroler","2003"),2003)
        self.assertEqual(ocekujemo, None)

if __name__ == '__main__':
    unittest.main()