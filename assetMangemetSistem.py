from dataclasses import dataclass
import socket
import mysql.connector
import os
from _thread import *
from mysql.connector import Error
#definisemo soket na koji ce sve stizati serveru
#bilo to preko kontrolera ili direktno od uredjaja
ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0 #ovo broji niti koliko imamo

##KONEKCIJA SA MYSQL
try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         database='bazaRes',
                                         password='stefan')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        #cursor.execute("CREATE DATABASE bazaRes;")
        cursor.execute("USE bazaRes;")
        cursor.execute("INSERT INTO uredjaji(id, vreme, trenutnaVrednost) VALUES('filip11', '2008-01-02 00:00:01', 'filip11');")
        connection.commit()
        record = cursor.fetchone()
        print("Uspesno ste konektovani na bazu: ", record)

except Error as e:
    print("Problem pri konektovanju na bazu ", e)

#cursor.execute("CREATE DATABASE BazaPodataka")
#cursor.execute("CREATE TABLE movies(title VARCHAR(50) NOT NULL,genre VARCHAR(30) NOT NULL,director VARCHAR(60) NOT NULL,release_year INT NOT NULL,PRIMARY KEY(title))")

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
        response = 'Poruka: ' + data.decode('utf-8')
        if not data:
            break
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