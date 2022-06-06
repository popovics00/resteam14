import socket
import sys 
import Kontroleri

#GLOBALNE
AMSSocket = socket.socket()
KontrolerSocket = socket.socket()
host = '127.0.0.1'
hostKontroler = '127.0.0.1'
port = 2004
portKontroler = 2005
tipUredjaja = 0
def konektujNaAMS():
    try:
        AMSSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    print('Cekamo na odgovor konekcije od strane AMS!')
    res = AMSSocket.recv(1024)
    

def konektujNaKontroler(portKontroler,tipUredjaja):
    try:
        KontrolerSocket.connect((hostKontroler, portKontroler))
    except socket.error as e:
        print(str(e))
    print('Cekamo na odgovor konekcije od strane Kontrolera!')
    res = KontrolerSocket.recv(1024)
    if tipUredjaja==1:
        temp = "register=analog/0"
        Send(str.encode(temp), KontrolerSocket)
    elif tipUredjaja==2:
        temp = "register=digital/0"
        Send(str.encode(temp), KontrolerSocket)

def KonektujSe():
    print("Odredi tip uredjaja >>\n 1 - Analogni \n 2 - Digitalni")
    tipUredjaja = int(input("-> "))

    print('Na koga se konektuje uredjaj >>\n')
    print('1 - Asset Menagement Sistem\n')
    print('2 - Lokalni kontroler\n')
    x = int(input("-> "))

    if x==1 :
        konektujNaAMS()
    elif x==2 :
        print("KONTROLERI NA RASPOLAGANJU")
        Kontroleri.Kontroleri.VratiKontolere()
        portKontroler = int(input("Odaberi port: "))
        konektujNaKontroler(portKontroler,tipUredjaja)
    else:
        print("Uneli ste pogresnu opciju za konektovanje")
        ZatvoriKonekciju()

    while True:
        if x==1 :
            Input = input('Unesi poruku AMS: ')
            Send(str.encode(Input), AMSSocket)
            if tipUredjaja==1 :
                AnalogniMenu()
            elif tipUredjaja ==2:
                DigitalniMenu()
            else:
                print("Nepostojeci tip uredjaja")
                break
        elif x==2 :
            Input = input('Unesi poruku KONTROLERU: ')
            Send(str.encode(Input), KontrolerSocket)
            if tipUredjaja==1 :
                AnalogniMenu()
            elif tipUredjaja ==2:
                DigitalniMenu()
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

def AnalogniMenu():
    print("Promena vrednosti analognog")

def DigitalniMenu():
    print("Izaberi komandu")
    print("1 - Upali / Otvori")
    print("2 - Ugasi / Zatvori")