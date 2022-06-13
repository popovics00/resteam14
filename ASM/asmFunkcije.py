from sqlite3 import Cursor
import mysql.connector
from mysql.connector import Error
class BazaPodataka:
    def __init__(self):
        self.connection =mysql.connector.connect(host='localhost',
                                                user='root',
                                                database='bazaRes',
                                                password='stefan')
        self.cursor = self.connection.cursor()

    def KonekcijaSaBazom(self):
        try:
            #self.connection = mysql.connector.connect(host='localhost',
            #                                    user='root',
            #                                    database='bazaRes',
            #                                    password='stefan')
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

        #cursor.execute("CREATE DATABASE bazaRes;")
        #cursor.execute("create table uredjaji(id VARCHAR(50) NOT NULL, vreme VARCHAR(50) NOT NULL , trenutnaVrednost VARCHAR(50) NOT NULL, PRIMARY KEY (id))")
    def CuvajUBazu(self, prvi, drugi, treci):
        self.cursor.execute("USE bazaRes;")
        #print(prvi)
        #print(drugi)
        #print(treci)
        #tempKomanda="INSERT INTO uredjaji(id, vreme, trenutnaVrednost) VALUES("+prvi+","+drugi+","+treci+");"
        try:
            tempKomanda="INSERT INTO uredjaji(id, vreme, trenutnaVrednost) VALUES('{0}', '{1}', '{2}');".format(prvi,drugi,treci)
            self.cursor.execute(tempKomanda)
        except:
            tempKomanda="UPDATE uredjaji set trenutnaVrednost = '{0}' where id = '{1}';".format(treci,prvi)
            self.cursor.execute(tempKomanda)

        self.connection.commit()