import sys
import cuvanjeKontrolera as Kontroleri
from tracemalloc import start
import storageFunkije as StorageUredjaj
import klasaLokalniUredjaj as lokalniUredjaj
import storageFunkije as storageFun
import socket
from _thread import *


ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0

KontrolerSideSocket = socket.socket()
hostKontroler = '127.0.0.1'
portKontroler = int(input("Unesi port -> "))

try:
    KontrolerSideSocket.bind((hostKontroler, portKontroler))
    ServerSideSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ServerSideSocket.recv(2048)

print('Soket je trenutno u osluskivanju zahteva od strane klijenta..')
KontrolerSideSocket.listen(5)
naz = "Kontoler"+str(portKontroler)
Kontroleri.CuvajKontrolere(portKontroler,naz)
storageUredjaja = storageFun.LocalDeviceStorage()

def multiThreadedClient(connection):
    connection.send(str.encode('Kontroler potvrdjuje da radi'))
    global startTime
    while True:
        data = connection.recv(2048)
        response = data.decode('utf-8')
        if not data:
            break
        #ServerSideSocket.send(data) #OVO TREBA ZAKOMENTARISATI
        print(response) #ispisujemo na kontroleru
        #OVDE UPISUJEMO U FAJL
        splitTemp = response.split("/")
        uredjajTemp = lokalniUredjaj.lokalniUredjaj(splitTemp[0], splitTemp[1], splitTemp[2])
        storageUredjaja.DodajNoviUredjaj(uredjajTemp,portKontroler)
        storageUredjaja.IscitajFajl(portKontroler,ServerSideSocket)
    connection.close()
while True:
    Client, address = KontrolerSideSocket.accept()
    print('Povezani ste upravo sa: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multiThreadedClient, (Client, ))
    ThreadCount += 1
    print('Broj niti: ' + str(ThreadCount))
Kontroleri.Brisanje(portKontroler)
KontrolerSideSocket.close()
ServerSideSocket.close()
