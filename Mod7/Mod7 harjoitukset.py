#monikko (tuple)

viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")

# joukko rakenne
pelit = {"Monopoli", "Shakki", "Cluedo"}
print(pelit)

pelit.add("Dominion")
print(pelit)

pelit.remove("Shakki")
print(pelit)

pelit.add("Cluedo")
print(pelit)

for p in pelit:
    print(p)

# tarkistaa löytyykö shakki pelien listalta.
if "shakki" in pelit:
    print("voidaan pelata shakkia")

# sanakirja
numerot = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"}

numerot["Olga"] = "050-1011012"
numerot["Mary"] = "0401-2132139"

print(numerot)

print(numerot["olga"])
while True:
    nimi = input("Anna nimi: ")
    if nimi in numerot:
        print (f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")

työntekijät = {
"Viivi" : ["Bulevardi","050-1234567"],
"Ahmed" : ["Tehtaankatu","040-1112223"],
"Pekka" : ["Liisankatu", "050-7654321"]}

tiedot = työntekijät["Viivi"]
print(tiedot[0])
print(tiedot[1])