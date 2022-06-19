import klasaXMLWritter as XMLWritter
import xml.etree.ElementTree as ET 
import klasaLokalniUredjaj as Kontroler
import sys

#testirano
def toString(text):
    try:
        return str(text)
    except:
        return "ERROR"

#ovde je pokriveno sve da ne baci gresku uz pomoc toString metode
def CuvajKontrolere(ports,name):
    lista=ET.parse("C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler\\kontroleriLista.xml")
    root=lista.getroot()
    
    kontroler=ET.SubElement(root,'Kontroler')
    
    port=ET.SubElement(kontroler,'port')
    naziv=ET.SubElement(kontroler,'naziv')
    port.text=toString(ports)
    naziv.text=toString(name)
    lista.write('C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler\\kontroleriLista.xml')

#ovde je pokriveno sve da ne baci gresku uz pomoc toString metode
def Brisanje(port):
    tempStr="C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler\\kontroleriLista.xml"
    lista=ET.parse(tempStr)
    root=lista.getroot()
    for kontroler in root:
        if kontroler[0].text==toString(port):
            root.remove(kontroler)
            lista.write(tempStr)

def MenuExit(portic):
    print("Unesi '!exit' kako bi ugasio kontroler");
    while True:
        x = input("->")
        if x=="!exit" :
            break
    Brisanje(portic)
    sys.exit()
    