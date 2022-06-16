import xml.etree.ElementTree as ET

def PreuzmiVreme():
    tempString = "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler\\vremeSlanja.xml"
    tree = ET.parse(tempString) 
    root = tree.getroot() 
    povratak = int(root[0].text)
    return povratak