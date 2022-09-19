# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
# ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta,
# helikopterikenttiä on 15 kappaletta jne.


import mysql.connector
# yhteyden avaus
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Sal41a6sana52S',
         autocommit=True
         )

CC = input("Anna maakoodi: ")
AP = "select type, count(*) from airport where iso_country = '" + CC + "' group by type"


kursori = yhteys.cursor()
kursori.execute(AP)

result = kursori.fetchall()

#kysytään lentokenttien lukumäärä suomessa järjesteltynä tyypin mukaan
print(f"Lentokentät tunnuksella: {CC}")
for rivi in result:
    print(f"{rivi[0]}, {rivi[1]}")