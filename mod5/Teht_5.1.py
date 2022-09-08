# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

import random
rollRes =[]
numdice = int(input("anna noppien määrä: "))
for i in range(numdice):
    roll = random.randint(1, 6)
    rollRes.append(roll)

print(sum(rollRes))

