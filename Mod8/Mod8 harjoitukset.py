import mysql.connector
# yhteyden avaus
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='',
         autocommit=True
         )
#määritellään kysely
ICAO = input("anna lentokentän ICAO: ")
sql = "select name, municipality from airport where ident ='" + ICAO + "'"

#suoritetaan kysely
kursori = yhteys.cursor()
kursori.execute(sql)

# haeaan ja käsitellään tulosrivit
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")