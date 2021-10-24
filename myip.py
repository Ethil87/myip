
import mysql.connector
import time
import datetime
import urllib.request
import config

my_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
print(my_ip)
my_ip_str = str(my_ip)

cnx = mysql.connector.connect(user=config.user, password=config.password,
                                      host=config.host, port=config.port,
                                      database=config.database)
cursor = cnx.cursor()

datanow = datetime.datetime.now().strftime("%Y-%m-%d")

query = ("INSERT INTO domoweip (adres,datanow) VALUES ( %s, %s)")

try:
        cursor.execute(query, (my_ip,datanow))
        print("Dane wyslane pomyslnie! ")
        cnx.commit()
except:
        print("Wystapil blad przy wysylaniu danych! ")
        cnx.rollback()

cursor.close()

cnx.close()

