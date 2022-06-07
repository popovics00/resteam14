import sys
import storageFunkije as LocalDeviceStorage
import klasaLokalniUredjaj as lokalniUredjaj
sys.path.insert(0,'C:\\Users\\stefa\\Desktop\\RES_Projekat\\Projekat2\\resteam14\\')
from lokalniUredjaj import Kontroleri
import storageFunkije as storageFun
import socket
import os
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
res = ServerSideSocket.recv(1024)

print('Soket je trenutno u osluskivanju zahteva od strane klijenta..')
KontrolerSideSocket.listen(5)
naz = "Kontoler"+str(portKontroler)
Kontroleri.Kontroleri.DodajUListu(int(portKontroler),naz)
Kontroleri.Kontroleri.VratiKontolere()

storageUredjaja = storageFun.LocalDeviceStorage()
uredjajTemp = lokalniUredjaj.lokalniUredjaj("stefan","stefan","stefan")
storageUredjaja.DodajNoviUredjaj(uredjajTemp,portKontroler)

def multiThreadedClient(connection):
    connection.send(str.encode('Kontroler potvrdjuje da radi'))
    while True:
        data = connection.recv(2048)
        response = 'Poruka: ' + data.decode('utf-8')
        if not data:
            break
        ServerSideSocket.send(data)
        print(response) #ispisujemo na kontroleru
    connection.close()
while True:
    Client, address = KontrolerSideSocket.accept()
    print('Povezani ste upravo sa: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multiThreadedClient, (Client, ))
    ThreadCount += 1
    print('Broj niti: ' + str(ThreadCount))
    Kontroleri.Kontroleri.VratiKontolere()

KontrolerSideSocket.close()
ServerSideSocket.close()
