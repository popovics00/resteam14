from ast import Try
from sqlite3 import Cursor
import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta
import sys
from colorama import Fore, Back, Style

class BazaPodataka:
    def __init__(self): #pragma:no cover
        self.connection =mysql.connector.connect(host='localhost',
                                                user='root',
                                                database='bazaRes',
                                                password='stefan')
        self.cursor = self.connection.cursor()
    
    #testirano na pravljenje vec postojece tabele
    def KonekcijaSaBazom(self):
        try:
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                komanda1="create table uredjajiLista(id VARCHAR(50) NOT NULL, vreme TIMESTAMP default current_timestamp , trenutnaVrednost VARCHAR(50) NOT NULL , vremeRada INT NOT NULL, PRIMARY KEY (id))"
                komanda2="create table uredjaji(id VARCHAR(50) NOT NULL, vreme TIMESTAMP default current_timestamp , trenutnaVrednost VARCHAR(50) NOT NULL)"
                try:
                    self.cursor.execute(komanda1)
                    self.cursor.execute(komanda2)
                except:
                    print("Pokusao sam da napravim tabele ali vec postoje.")
                    return "ERROR"
        except Error as e:
            print("Problem pri konektovanju na bazu ", e)
            return "ERROR"
    
    def CuvajUBazu(self, prvi, drugi, treci): #pragma:no cover
        self.cursor.execute("USE bazaRes;")
        helperDrugi = "STR_TO_DATE('"+drugi+"', '%Y-%m-%d %H:%i:%s.%f')"
        try:
            #DODAJEMO U OBE TABELE
            tempKomanda="INSERT INTO uredjaji(id, vreme, trenutnaVrednost) VALUES('{0}', {1}, '{2}');".format(prvi,helperDrugi,treci)
            self.cursor.execute(tempKomanda)
            tempKomanda="INSERT INTO uredjajiLista(id, vreme, trenutnaVrednost,vremeRada) VALUES('{0}', {1}, '{2}',0);".format(prvi,helperDrugi,treci)
            self.cursor.execute(tempKomanda)
        except:
            tempKomanda="UPDATE uredjajiLista set trenutnaVrednost = '{0}',vreme = {1} where id = '{2}';".format(treci,helperDrugi,prvi)
            self.cursor.execute(tempKomanda)
        self.connection.commit()
    
    #testirano sa nepostojecim tabelama
    def IspisiSve(self,tabela):
        try:
            self.cursor.execute("SELECT * FROM "+tabela)
            result = self.cursor.fetchall()

            print("\n\nISPIS SVIH UREDJAJA:")
            for row in result:
                print(" ID Uredjaja: "+row[0]+" | Stanje: "+row[2]+" | Poslednja izmena: "+row[1].strftime('%m/%d/%Y'))
        except:
            return "ERROR"

    #3 - Izlistavanje svih uredjaja čiji je broj radnih sati preko konfigurisane vrednosti (alarmirati i obojiti u crvenu boju one uređaje za koje je broj radnih sati veći od granice definisane u opcijama aplikacije)
    def RacunajSvimaRadneSate(self,alarmGranica):
        query="select * from uredjajiLista"
        try:
            self.cursor.execute(query)
        except:
            return "ERROR"
        
        FMT = '%Y-%m-%d %H:%i:%s'
        listaUredjaja = self.cursor.fetchall()
        
        for row in listaUredjaja:
            self.RacunajRadneSate("01/01/0001","31/12/9999",row[0],"YES",alarmGranica) #da ne kucamo ponovo samo napravimo poziv postojee funkcije

    def RacunajRadneSate(self,odDatuma, doDatuma,id,ispis,alarmGranica):
        #Broj radnih sati za izabrani uredjaj za izabrani vremenski period (od – do kalendarski po satima)
        odTemp = KomandaZaDatum(odDatuma)
        doTemp = KomandaZaDatum(doDatuma)
        #prikaz svih sa tim id u tom vremenu po rastucem redosledu vremena kako bi analizirali redom
        query="select * from uredjaji where vreme>={0} and vreme<={1} and id='{2}' order by vreme ASC".format(odTemp,doTemp,id)
        try:
            self.cursor.execute(query)
        except:
            return "ERROR"
        
        FMT = '%Y-%m-%d %H:%i:%s'
        result = self.cursor.fetchall()
        #print(FMT)
        #print(result[0][1])
        rvreme = result[0][1]-result[0][1]#datetime.strftime(result[0][1],FMT)
        tempStart =result[0][1]
        tempEnd=result[0][1]
        prethodnoStanje=""
        for row in result:
            if row[2]=="OFF" or row[2]=="0":
                #print("Sada je ugasen pa zavrsavamo vreme i upisujemo u sumu vremena")
                tempEnd=row[1]
                if prethodnoStanje == "ON":
                    rvreme = rvreme + (tempEnd-tempStart)
                #print("OVO JE VREME" + str(rvreme))
                tempStart=tempEnd
                prethodnoStanje="OFF"
            elif row[2]!="OFF": #ako je neki broj ili ON
                #print("Sada je upaljen i krecemo racunanje vremena")
                #print("OVO JE VREME" + str(rvreme))
                tempStart=row[1]
                prethodnoStanje="ON"
        sec=rvreme.total_seconds()
        if ispis=="YES":
            if sec <= alarmGranica:
                print(Fore.RED+"ID: {0} | RadnoVreme: {1} ".format(id,rvreme)+Fore.WHITE)
                #print(Fore.WHITE)
            elif sec >alarmGranica:
                print(Fore.GREEN+"ID: {0} | RadnoVreme: {1} ".format(id,rvreme)+Fore.WHITE)
                #print(Fore.WHITE)

        tempKomanda="UPDATE uredjajiLista set vremeRada = {0} where id = '{1}';".format(int(sec),id)
        
        try:
            self.cursor.execute(tempKomanda)
            self.connection.commit()
            return int(sec)
        except:
            return "ERROR"

    #testirano
    def VratiPoVremenu(self,odDatuma,doDatuma,id):
        #odSplit=odDatuma.split("/")
        #doSplit=doDatuma.split("/")
        #odTemp="STR_TO_DATE('{0}-{1}-{2} 0:00:00.100000', '%d-%m-%Y %H:%i:%s.%f')".format(odSplit[0],odSplit[1],odSplit[2])
        #doTemp="STR_TO_DATE('{0}-{1}-{2} 0:00:00.100000', '%d-%m-%Y %H:%i:%s.%f')".format(doSplit[0],doSplit[1],doSplit[2])
        odTemp = KomandaZaDatum(odDatuma)
        doTemp = KomandaZaDatum(doDatuma)
        query="select * from uredjaji where vreme>={0} and vreme<={1} and id='{2}'".format(odTemp,doTemp,id)
        try:
            self.cursor.execute(query)
        except:
            return "ERROR"
        
        try:
            result = self.cursor.fetchall()
            print("\n\nVREDNOSTI za period od "+odDatuma+" do "+doDatuma+"\n")
            for row in result:
                print(" ID Uredjaja: "+row[0]+" | Stanje setovano na: "+row[2]+" | Vreme izmene: "+row[1].strftime('%m/%d/%Y'))
        except:
            return "ERROR"
            print("!! - NEMA VREDNOSTI U TOM PERIODU")
    
    #unos sa tastature nema potrebe testirati jer toInt je vec testirana
    def AsmMenu(self):
        while True:
            print("\n\nIzaberite opciju koju zelite za prikaz:")
            print("1 - Detalji promena za izabrani period za izabrani lokalni uređaj (sve promene + sumarno)")
            print("2 - Broj radnih sati za izabrani uredjaj za izabrani vremenski period (od – do kalendarski po satima)")
            print("#3 - Izlistavanje svih uredjaja čiji je broj radnih sati preko konfigurisane vrednosti (alarmirati i obojiti u crvenu boju one uređaje za koje je broj radnih sati veći od granice definisane u opcijama aplikacije)")
            print("4 - Listanje svih postojećih uređaja u sistemu")
            print("\nZA GASENJE PROGRAMA STISNI BILO STA SEM PONUDJENIH")
            x = toInt(input("-> "))
            if x==4:
                self.IspisiSve("uredjajiLista")
            elif x==1:
                print("FORMAT DATUMA: DAN/MESEC/GODINA")
                od=input('od: ')
                do=input('do: ')
                uredjaj=input('uredjaj -> ')
                try:
                    self.VratiPoVremenu(od,do,uredjaj) 
                except:
                    print("Pogresno unete vrednosti (verovatno pogresan format datuma)") 
                    return "ERROR"
            elif x==2:
                print("FORMAT DATUMA: DAN/MESEC/GODINA")
                #od=input('od: ')
                #do=input('do: ')
                od="02/02/2010"
                do="20/10/2025"
                uredjaj=input('uredjaj -> ')
                print("Uredjaj sa {0} ima {1} sekundi aktivnost u periodu od {2} do {3}".format(uredjaj,self.RacunajRadneSate(od, do,uredjaj,"NO",0),od,do,))
            elif x==3:
                alarmGranica = int(input("Unesite granicu alarma -> "))
                self.RacunajSvimaRadneSate(alarmGranica)
            else:
                print("Izlazak iz programa")
                sys.exit()

#testirano
def toInt(broj):
    try:
        return int(broj)
    except:
        return "ERROR"

#testirano
def KomandaZaDatum(datum):
    try:
        d=datum.split("/")
        datTemp="STR_TO_DATE('{0}-{1}-{2} 0:00:00.100000', '%d-%m-%Y %H:%i:%s.%f')".format(d[0],d[1],d[2])
        return datTemp
    except:
        return "ERROR"