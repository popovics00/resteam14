import socket
import os
from _thread import *
ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0

KontrolerSideSocket = socket.socket()
hostKontroler = '127.0.0.1'
portKontroler = 2005
try:
    KontrolerSideSocket.bind((hostKontroler, portKontroler))
    ServerSideSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ServerSideSocket.recv(1024)
print('Socket is listening..')
KontrolerSideSocket.listen(5)
def multi_threaded_client(connection):
    connection.send(str.encode('Kontroler potvrdjuje da radi'))
    while True:
        data = connection.recv(2048)
        response = 'Poruka: ' + data.decode('utf-8')
        if not data:
            break
        ServerSideSocket.send(data)
        #ServerSideSocket.send(str.encode(response)) #kontroler prosledjuje na soket od AMS
        print(response) #ispisujemo na kontroleru
        #connection.sendall(str.encode(response))
    connection.close()
while True:
    Client, address = KontrolerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
KontrolerSideSocket.close()
ServerSideSocket.close()