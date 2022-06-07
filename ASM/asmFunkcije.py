import mysql.connector
from mysql.connector import Error

def konekcijaSaBazom():
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
