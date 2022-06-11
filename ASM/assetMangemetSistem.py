from dataclasses import dataclass
import socket
import os
from _thread import *
import asmFunkcije as Baza

#definisemo soket na koji ce sve stizati serveru
#bilo to preko kontrolera ili direktno od uredjaja
ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0 #ovo broji niti koliko imamo

bazaPodataka = Baza.BazaPodataka()

try:
    ServerSideSocket.bind((host, port)) #pokusavamo da bindujemo na adresu i port
except socket.error as e:
    print(str(e))

print('[ALERT] Socket trenutno osluskuje i ocekuje poruke..')
ServerSideSocket.listen(5)
def multi_threaded_client(connection):
    connection.send(str.encode('Server potrvrdjuje da radi!'))
    while True:
        data = connection.recv(2048)
        response = data.decode('utf-8')
        if not data:
            break
        splitTemp = response.split("/")
        #uredjajTemp = lokalniUredjaj.lokalniUredjaj(splitTemp[0], splitTemp[1], splitTemp[2])
        bazaPodataka.KonekcijaSaBazom()
        bazaPodataka.CuvajUBazu(splitTemp[0],splitTemp[1],splitTemp[2])
        print(response) #ispis na serveru
        #connection.sendall(str.encode(response))    #potvrdjujemo da je poruka primljena
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))

if connection.is_connected():
    cursor.close()
    connection.close()
    print("Konekcija sa bazom je prekinuta")
ServerSideSocket.close()