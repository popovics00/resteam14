import klasaXMLWritter as XMLWritter
import xml.etree.ElementTree as ET 
import klasaLokalniUredjaj as Kontroler

def CuvajKontrolere(ports,name):
    lista=ET.parse("C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler\\kontroleriLista.xml")
    root=lista.getroot()
    
    kontroler=ET.SubElement(root,'Kontroler')
    
    port=ET.SubElement(kontroler,'port')
    naziv=ET.SubElement(kontroler,'naziv')
    port.text=str(ports)
    naziv.text=str(name)
    lista.write('C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler\\kontroleriLista.xml')

def Brisanje(port):
    lista=ET.parse("C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler\\kontroleriLista.xml")
    root=lista.getroot()
    for kontroler in root:
        if kontroler[0].text==str(port):
            root.remove(kontroler)
