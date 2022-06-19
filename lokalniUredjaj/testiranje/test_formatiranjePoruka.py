import unittest
import sys 
from datetime import datetime
import os
import time
sys.path.insert(0, "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniUredjaj")
from uredjajFunkcije import FormatirajPoruku

#        temp=FormatirajPoruku(idTemp,str(datetime.now()),"ON")
class MyTestCase(unittest.TestCase):
    def test_case1(self):
        tempVreme=str(datetime.now())
        stringNew="3/"+tempVreme+"/ON/"
        ocekujemo = FormatirajPoruku(3,tempVreme,"ON")
        self.assertEqual(ocekujemo, stringNew)

    def test_case2(self):
        tempVreme=str(datetime.now())
        stringNew="idTemp/"+tempVreme+"/ON/"
        ocekujemo = FormatirajPoruku("idTemp",tempVreme,"ON")
        self.assertEqual(ocekujemo, stringNew)


if __name__ == '__main__':
    unittest.main()