from multiprocessing.connection import wait
import klasaLokalniUredjaj as LU
import klasaXMLWritter as XMLWritter
import xml.etree.ElementTree as ET 
import os
import time
class LocalDeviceStorage:
    def __init__(self):
        self.uredjaji = []


    def DodajNoviUredjaj(self, uredjajDodaj:LU.lokalniUredjaj, port):
        self.uredjaji.append(vars(uredjajDodaj))
        dodaj = {'SpisakUredjaja': {'LokalniUredjaj': self.uredjaji}}
        xmlWritter = XMLWritter.XMLWritter(dodaj)
        tempString = "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler\\kontroler" + str(port) + ".xml"
        f = open(tempString, "w")
        f.write(xmlWritter.doc.toxml("UTF-8").decode("UTF=8"))

    def IscitajFajl(self,port,saljiNaSoket):
        tempString = "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler\\kontroler" + str(port) + ".xml"
        tree = ET.parse(tempString) 
        root = tree.getroot() 

        for lu in root.findall('LokalniUredjaj'):
            tempText = lu[0].text+'/'+lu[1].text+'/'+lu[2].text
            saljiNaSoket.send(str.encode(tempText))
        time.sleep(5)
        os.remove(tempString)



