import unittest
import sys 
from datetime import datetime
import os
import time
sys.path.insert(0, "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniUredjaj")
from uredjajFunkcije import AnalogniMenu

class MyTestCase(unittest.TestCase):
    def test_case1(self):
        ocekujemo = AnalogniMenu(3)
        self.assertEqual(ocekujemo, "ERROR")

    def test_case2(self):
        ocekujemo = AnalogniMenu("text")
        self.assertEqual(ocekujemo, "ERROR")


if __name__ == '__main__':
    unittest.main()