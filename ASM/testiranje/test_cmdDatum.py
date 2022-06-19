import unittest
import sys 
import os
sys.path.insert(0, "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\ASM")
from asmFunkcije import KomandaZaDatum


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        temp = KomandaZaDatum("321/31")
        self.assertEqual(temp, "ERROR")

    def test_case2(self):
        temp = KomandaZaDatum("321.321")
        self.assertEqual(temp, "ERROR")
    
    def test_case3(self):
        datum = "06/11/2020"
        d=datum.split("/")
        datTemp="STR_TO_DATE('{0}-{1}-{2} 0:00:00.100000', '%d-%m-%Y %H:%i:%s.%f')".format(d[0],d[1],d[2])

        temp = KomandaZaDatum(datum)
        self.assertEqual(temp, datTemp)
    
    def test_case4(self):
        temp = KomandaZaDatum("/")
        self.assertEqual(temp, "ERROR")



if __name__ == '__main__':
    unittest.main()