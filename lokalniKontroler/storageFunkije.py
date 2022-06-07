import klasaLokalniUredjaj as LU
import klasaXMLWritter as XMLWritter

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

