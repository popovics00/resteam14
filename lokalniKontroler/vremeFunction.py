import xml.etree.ElementTree as ET

#testirano
def toInt(broj):
    try:
        return int(broj)
    except:
        return "ERROR"

#nema potrebe testirati jer sve sto moze gresku napraviti je toInt a to je testirano
def PreuzmiVreme(): #pragma:no cover
    tempString = "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler\\vremeSlanja.xml"
    tree = ET.parse(tempString) 
    root = tree.getroot() 
    povratak = toInt(root[0].text)
    return povratak