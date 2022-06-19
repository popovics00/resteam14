from msilib.schema import Error
import socket
from datetime import datetime
import xml.etree.ElementTree as ET 
import sys
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

#nema potrebe za testiranjem jer ne saljemo neku povratnu vrednost jer se konektujemo stalno na isti port
#jedino da se desi da AMS nije startan ali to resava Exception i test za probajInt
def konektujNaAMS(): #pragma:no cover
    try:
        AMSSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    print('Cekamo na odgovor konekcije od strane AMS!')
    res = AMSSocket.recv(1024)
    global idTemp
    idTemp = input("Unesite ID uredjaja -> ")
    global stanjeTemp
    stanjeTemp = input("Unesite pocetno stanje/vrednost -> ")

    if stanjeTemp=="ON" and tipUredjaja==2: 
        temp="{0}/{1}/{2}".format(idTemp,str(datetime.now()),stanjeTemp)
        Send(str.encode(temp), AMSSocket)
    elif stanjeTemp =="OFF" and tipUredjaja==2: 
        temp="{0}/{1}/{2}".format(idTemp,str(datetime.now()),stanjeTemp)
        Send(str.encode(temp), AMSSocket)
    elif (probajInt(stanjeTemp) != "ERROR") and tipUredjaja==1:
        temp="{0}/{1}/{2}".format(idTemp,str(datetime.now()),stanjeTemp)
        Send(str.encode(temp), AMSSocket)
    else:
        print("Greska pri unosu pocetnog stanja/vrednosti")
        ZatvoriKonekciju()
    
#testirano da li su prosledjeni dobri parametri
def konektujNaKontroler(portKontroler,tipUredjaja):
    try:
        KontrolerSocket.connect((hostKontroler, portKontroler))
    except:
        print("Prosledili ste pogresan host ili tip uredjaja.")
        return "ERROR"
    print('Cekamo na odgovor konekcije od strane Kontrolera!')
    res = KontrolerSocket.recv(1024)
    global idTemp
    idTemp = input("Unesite ID uredjaja -> ")
    global stanjeTemp
    stanjeTemp = input("Unesite pocetno stanje/vrednost -> ")
    
    if stanjeTemp=="ON" and tipUredjaja==2: 
        temp="{0}/{1}/{2}".format(idTemp,str(datetime.now()),stanjeTemp)
        Send(str.encode(temp), KontrolerSocket)
    elif stanjeTemp =="OFF" and tipUredjaja==2: 
        temp="{0}/{1}/{2}".format(idTemp,str(datetime.now()),stanjeTemp)
        Send(str.encode(temp), KontrolerSocket)
    elif (probajInt(stanjeTemp) != "ERROR") and tipUredjaja==1:
        temp="{0}/{1}/{2}".format(idTemp,str(datetime.now()),stanjeTemp)
        Send(str.encode(temp), KontrolerSocket)
    else:
        print("Greska pri unosu pocetnog stanja/vrednosti")
        ZatvoriKonekciju()

#testirano da li je uspena konverzija u int
def probajInt(broj):
    try:
        return int(broj)
    except:
        return "ERROR"



def KonektujSe(): #pragma:no cover
    print("Odredi tip uredjaja >>\n 1 - Analogni \n 2 - Digitalni")
    global tipUredjaja
    tipUredjaja = probajInt(input("-> "))
    
    if tipUredjaja=="ERROR":
        print("Zatvori konekciju unet pogresni tip uredjaja!")
        ZatvoriKonekciju()
    
    print('Na koga se konektuje uredjaj >>')
    print('1 - Asset Menagement Sistem')
    print('2 - Lokalni kontroler')
    
    x = probajInt(input("-> "))
    if x=="ERROR":
        print("Probem pri odabiru nacina pozevivanja!")
        ZatvoriKonekciju()

    if x==1 :
        konektujNaAMS()
    elif x==2 :
        print("\n\nKONTROLERI NA RASPOLAGANJU")
        IscitajKontrolere()
        portKontroler = probajInt(input("Odaberi port: "))
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
                ZatvoriKonekciju()
        elif x==2 :
            if tipUredjaja==1 :
                AnalogniMenu(KontrolerSocket)
            elif tipUredjaja ==2:
                DigitalniMenu(KontrolerSocket)
            else:
                print("Nepostojeci tip uredjaja")
                ZatvoriKonekciju()
        else :
            print("Neuspesno slanje!")
            ZatvoriKonekciju()

def Send (poruka, soket): #pragma:no cover
    try:
        soket.send(poruka)
    except:
        print("Doslo je do greske u slanju poruke na odredjeni soket")

def ZatvoriKonekciju(): #pragma:no cover
    AMSSocket.close()
    KontrolerSocket.close()
    return("ERROR")

#pokriveno sa probaj int
def AnalogniMenu(soket): #pragma:no cover
    print("Promena vrednosti analognog")
    stanjeTemp = input("-> ")
    if probajInt(stanjeTemp)!="ERROR":
        temp="{0}/{1}/{2}/".format(idTemp,str(datetime.now()),probajInt(stanjeTemp))
        Send(str.encode(temp), soket)
    else:
        print("Neodgovarajuca vrednost izmene, unesite broj")
        
#pokriveno sa formatiranjem poruka
def DigitalniMenu(soket): #pragma:no cover
    print("Izaberi komandu")
    print("1 - Upali / Otvori")
    print("2 - Ugasi / Zatvori")
    stanjeTemp = input("-> ")
    if stanjeTemp=="1":
        #temp="{0}/{1}/{2}/".format(idTemp,str(datetime.now()),"ON")
        temp=FormatirajPoruku(idTemp,str(datetime.now()),"ON")
        Send(str.encode(temp), soket)
    elif stanjeTemp=="2":
        #temp="{0}/{1}/{2}/".format(idTemp,str(datetime.now()),"OFF")
        temp=FormatirajPoruku(idTemp,str(datetime.now()),"OFF")
        Send(str.encode(temp), soket)

#testirano
def FormatirajPoruku(prvi,drugi,treci):
    try:
        temp="{0}/{1}/{2}/".format(prvi,drugi,treci)
        return temp
    except:
        return "ERROR"


def IscitajKontrolere(): #pragma:no cover
        tempString = "C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\lokalniKontroler\\kontroleriLista.xml"
        try:
            tree = ET.parse(tempString) 
            root = tree.getroot() 
        except:
            return "ERROR"

        for kon in root.findall('Kontroler'):
            tempText = kon[0].text+' sa portom '+kon[1].text
            print(tempText)