import socket
import xml.etree.ElementTree as ET
import calendar
import time

brojac = 0
current_GMT = time.gmtime()
time_stamp = calendar.timegm(current_GMT)

#tree = ET.parse('config.xml')
#root = tree.getroot()
#imeUredjaja = ET.Element("imeUredjaja")
#imeUredjaja.text = str(hash('test'))
#root.append(imeUredjaja)
#timeStamp = ET.Element("timeStamp")
#timeStamp.text = str(time_stamp)
#root.append(timeStamp)
#trenutnaVrednost = ET.Element("trenutnaVrednost")
#trenutnaVrednost.text = "off"
#root.append(trenutnaVrednost)
#ET.dump(root)


ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

KontrolerMultiSocket = socket.socket()
hostKontroler = '127.0.0.1'
portKontroler = 2005
try:
    KontrolerMultiSocket.connect((hostKontroler, portKontroler))
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
print('Cekamo na odgovor konekcije!')
res = KontrolerMultiSocket.recv(1024)
res = ClientMultiSocket.recv(1024)

print('Na koga se konektuje uredjaj >>\n')
print('1 - Asset Menagement Sistem\n')
print('2 - Lokalni kontroler\n')   
x = int(input("-> "))
while True:

    if x==1 :
        Input = input('Unesi poruku SERVISU: ')
        ClientMultiSocket.send(str.encode(Input))
        #res = ClientMultiSocket.recv(1024)
        #print(res.decode('utf-8'))
    else :
        Input = input('Unesi poruku KONTROLERU: ')
        KontrolerMultiSocket.send(str.encode(Input))
ClientMultiSocket.close()
KontrolerMultiSocket.close()