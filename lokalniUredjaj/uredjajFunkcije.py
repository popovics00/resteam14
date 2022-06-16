import socket
from datetime import datetime
import xml.etree.ElementTree as ET 

#GLOBALNE
AMSSocket = socket.socket()
KontrolerSocket = socket.socket()
host = '127.0.0.1'
hostKontroler = '127.0.0.1'
port = 2004
portKontroler = 2005
tipUredjaja = 0
idTemp = ""
stanjeTemp=""

def konektujNaAMS():
    try:
        AMSSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    print('Cekamo na odgovor konekcije od strane AMS!')
    res = AMSSocket.recv(1024)
    global idTemp
    idTemp = input("Unesite ID uredjaja -> ")
    global stanjeTemp
    stanjeTemp = input("Unesite pocetno stanje -> ")
    temp="{0}/{1}/{2}".format(idTemp,str(datetime.now()),stanjeTemp)
    Send(str.encode(temp), AMSSocket)
    

def konektujNaKontroler(portKontroler,tipUredjaja):
    try:
        KontrolerSocket.connect((hostKontroler, portKontroler))
    except socket.error as e:
        print(str(e))
    print('Cekamo na odgovor konekcije od strane Kontrolera!')
    res = KontrolerSocket.recv(1024)
    global idTemp
    global stanjeTemp
    if tipUredjaja==1:
        #ANALOG
        idTemp = input("Unesite ID uredjaja -> ")
        stanjeTemp = input("Unesite pocetno stanje -> ")
        temp="{0}/{1}/{2}/".format(idTemp,str(datetime.now()),stanjeTemp)
        Send(str.encode(temp), KontrolerSocket)
    elif tipUredjaja==2:
        #DIGITAL
        idTemp = input("Unesite ID uredjaja -> ")
        stanjeTemp = input("Unesite pocetno stanje -> ")
        temp="{0}/{1}/{2}/".format(idTemp,str(datetime.now()),stanjeTemp)
        Send(str.encode(temp), KontrolerSocket)
        
def KonektujSe():
    print("Odredi tip uredjaja >>\n 1 - Analogni \n 2 - Digitalni")
    tipUredjaja = int(input("-> "))

    print('Na koga se konektuje uredjaj >>')
    print('1 - Asset Menagement Sistem')
    print('2 - Lokalni kontroler')
    x = int(input("-> "))

    if x==1 :
        konektujNaAMS()
    elif x==2 :
        print("KONTROLERI NA RASPOLAGANJU")
        IscitajKontrolere()
        portKontroler = int(input("Odaberi port: "))
        konektujNaKontroler(portKontroler,tipUredjaja)
    else:
        print("Uneli ste pogresnu opciju za konektovanje")
        ZatvoriKonekciju()

    while True:
        if x==1 :
            if tipUredjaja==1 :
                AnalogniMenu(AMSSocket)
            elif tipUredjaja ==2:
                DigitalniMenu(AMSSocket)
            else:
                print("Nepostojeci tip uredjaja")
                break
        elif x==2 :
            if tipUredjaja==1 :
                AnalogniMenu(KontrolerSocket)
            elif tipUredjaja ==2:
                DigitalniMenu(KontrolerSocket)
            else:
                print("Nepostojeci tip uredjaja")
                break
        else :
            print("Neuspesno slanje!")
            break

def Send (poruka, soket):
    host = '127.0.0.1'
    soket.send(poruka)

def ZatvoriKonekciju():
    AMSSocket.close()
    KontrolerSocket.close()

def AnalogniMenu(soket):
    print("Promena vrednosti analognog")
    stanjeTemp = input("-> ")
    temp="{0}/{1}/{2}/".format(idTemp,str(datetime.now()),stanjeTemp)
    Send(str.encode(temp), soket)

def DigitalniMenu(soket):
    print("Izaberi komandu")
    print("1 - Upali / Otvori")
    print("2 - Ugasi / Zatvori")
    stanjeTemp = input("-> ")
    if stanjeTemp=="1":
        temp="{0}/{1}/{2}/".format(idTemp,str(datetime.now()),"ON")
        Send(str.encode(temp), soket)
    elif stanjeTemp=="2":
        temp="{0}/{1}/{2}/".format(idTemp,str(datetime.now()),"OFF")
        Send(str.encode(temp), soket)

def IscitajKontrolere():
        tempString = "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler\\kontroleriLista.xml"
        tree = ET.parse(tempString) 
        root = tree.getroot() 

        for kon in root.findall('Kontroler'):
            tempText = kon[0].text+' sa portom '+kon[1].text
            print(tempText)