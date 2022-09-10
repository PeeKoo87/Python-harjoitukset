# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def PizzanArvo(halkaisijaCm, hinta):
    sade = float(halkaisijaCm / 2)
    pintaAlaM = (math.pi * sade * sade) / 10000
    arvo = hinta / pintaAlaM
    return arvo

pizzat = []

for x in range(2):
    print(f"Anna pizza {x} tiedot!")
    hinta = float(input("Syötä pizzan hinta"))
    halkaisija = float(input("Syötä pizzan halkaisija: "))
    pizzat.append(PizzanArvo(halkaisija, hinta))

arvokkaimmanId = 0
for x in range(2):
    if pizzat[arvokkaimmanId] > pizzat[x]:
        arvokkaimmanId = x

print(f"Arvokkain (paras hinta-kokosuhde) pizza on indeksin {arvokkaimmanId}. pizza")