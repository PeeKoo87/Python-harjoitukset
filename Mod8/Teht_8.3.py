# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
# ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)


from geopy import distance

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

def haku(icao):
    icao = input("syötä aseman ICAO-koodi:")
    sql = "select latitude_deg, longitude_deg from airport where gps_code = "'" + icao + "'

    # suoritetaan kysely
    kursori = yhteys.cursor()
    kursori.execute(sql)
    response = kursori.fetchall() # tai .fetchone()
    if kursori.rowcount > 0:
        return response[0]
    else:
        print("kenttää ei löydy")

print(" lasketaan kanhden lentokentän etäisyys\n")
locations = []
for i in range(2):
    icao = input(f"syötä {i+1}. lentokentän ICAO:")
    loc1 = haku(icao)
    locations.append(haku(icao))
print(locations)

print(loc1)
print(type(loc1))


gap = distance.distance(locations[0], locations[1]).km
print(gap)
print(type(gap))
print(f"lentokenttien välinen etäisyys on {gap:.2f} km")