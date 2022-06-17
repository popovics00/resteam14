from sqlite3 import Cursor
import mysql.connector
from mysql.connector import Error
from datetime import date

class BazaPodataka:
    def __init__(self):
        self.connection =mysql.connector.connect(host='localhost',
                                                user='root',
                                                database='bazaRes',
                                                password='stefan')
        self.cursor = self.connection.cursor()

    def KonekcijaSaBazom(self):
        try:
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                #self.cursor = self.connection.cursor()
                #OVO PRVI PUT DA NAPRAVIMO BAZU
                #cursor.execute("CREATE DATABASE bazaRes;")
                record = self.cursor.fetchone()
                print("Uspesno ste konektovani na bazu: ", record)
                #self.cursor.execute("CREATE TABLE uredjaji")

        except Error as e:
            print("Problem pri konektovanju na bazu ", e)

        #cursor.execute("create table uredjaji(id VARCHAR(50) NOT NULL, vreme VARCHAR(50) NOT NULL , trenutnaVrednost VARCHAR(50) NOT NULL, PRIMARY KEY (id))")
    
    def CuvajUBazu(self, prvi, drugi, treci):
        self.cursor.execute("USE bazaRes;")
        #try:
        #INSERT INTO uredjaji VALUES('1',STR_TO_DATE("23-12-2012 18:00:00.100000", "%Y-%m-%d %H:%i:%s.%f"),'OPEN')
        helperDrugi = "STR_TO_DATE('"+drugi+"', '%Y-%m-%d %H:%i:%s.%f')"
        tempKomanda="INSERT INTO uredjaji(id, vreme, trenutnaVrednost) VALUES('{0}', {1}, '{2}');".format(prvi,helperDrugi,treci)
        self.cursor.execute(tempKomanda)
        #except:
            #tempKomanda="UPDATE uredjaji set trenutnaVrednost = '{0}' where id = '{1}';".format(treci,prvi)
            #self.cursor.execute(tempKomanda)
        self.connection.commit()

    def IspisiSve(self):
        self.cursor.execute("SELECT * FROM uredjaji")
        result = self.cursor.fetchall()
        print("\n\nISPIS SVIH UREDJAJA:")
        for row in result:
            print(" ID Uredjaja: "+row[0]+" | Stanje: "+row[2]+" | Poslednja izmena: "+row[1].strftime('%m/%d/%Y'))

    def VratiPoVremenu(self,odDatuma,doDatuma,id):
        #INSERT INTO uredjaji VALUES('1',STR_TO_DATE("23-12-2012 18:00:00.100000", "%d-%m-%Y %H:%i:%s.%f"),'OPEN')
        odSplit=odDatuma.split("/")
        doSplit=doDatuma.split("/")
        odTemp="STR_TO_DATE('{0}-{1}-{2} 0:00:00.100000', '%d-%m-%Y %H:%i:%s.%f')".format(odSplit[0],odSplit[1],odSplit[2])
        doTemp="STR_TO_DATE('{0}-{1}-{2} 0:00:00.100000', '%d-%m-%Y %H:%i:%s.%f')".format(doSplit[0],doSplit[1],doSplit[2])
        #print(odTemp)
        #print(doTemp)
        query="select * from uredjaji where vreme>={0} and vreme<={1} and id='{2}'".format(odTemp,doTemp,id)
        self.cursor.execute(query)
        try:
            result = self.cursor.fetchall()
            print("\n\nVREDNOSTI za period od "+odDatuma+" do "+doDatuma+"\n")
            for row in result:
                print(" ID Uredjaja: "+row[0]+" | Stanje setovano na: "+row[2]+" | Vreme izmene: "+row[1].strftime('%m/%d/%Y'))
        except:
            print("!! - NEMA VREDNOSTI U TOM PERIODU")
    def AsmMenu(self):
        while True:
            print("\n\nIzaberite opciju koju zelite za prikaz:")
            print("1 - Detalji promena za izabrani period za izabrani lokalni uređaj (sve promene + sumarno)")
            print("2 - Broj radnih sati za izabrani uredjaj za izabrani vremenski period (od – do kalendarski po satima)")
            print("3 - Izlistavanje svih uredjaja čiji je broj radnih sati preko konfigurisane vrednosti (alarmirati i obojiti u crvenu boju one uređaje za koje je broj radnih sati veći od granice definisane u opcijama aplikacije)")
            print("4 - Listanje svih postojećih uređaja u sistemu")
            x = int(input("-> "))
            if x==4:
                self.IspisiSve()
            elif x==2:
                print("FORMAT DATUMA: DAN/MESEC/GODINA")
                od=input('od: ')
                do=input('do: ')
                uredjaj=input('uredjaj -> ')
                try:
                    self.VratiPoVremenu(od,do,uredjaj) 
                except:
                    print("Pogresno unete vrednosti") 
            else:
                print("Nepostojeca opcija")
            #elif x==2:
            #elif x==1:
