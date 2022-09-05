import random
numberofrounds = int(input("monta numeroa luupataan"))

i = 0
while i <numberofrounds:

#while i < 10:  # ehdosta tulee aina arvo True tai False
    i +=1
    print(f"i = {i-1}+ 1 ->{i}")
    #tulostetaan parittomat luvut
    if i % 2 == 1:
        print(f"{i} on pariton")
    #i += 2  # i = i + 2
    #print(f"i = i + 2 -> {i}")

print(f"i: arvon silmukan jälkeen {i}")


#tekstikäytööliittymällisen ohjelman valikko

#komento = input ("Anna komento: ")
#while komento!="lopeta":
   # print ("Suoritan toiminnon: " + komento)
    #komento = input("Anna komento: ")
#print ("Toiminnot lopetettu.")
command = ""
while command != "lopeta":          #while true jatkaa looppia loputtomiin
    command = input("komento> ")
    #muutetaan command arvo pieniksi kirjaimiksi
    command = command.lower()
    #print(f"suoritetaan toiminto {command}")
    if command == "tulosta":
        print("printtaillaan jotain")
    elif command == "piirrä" or command == "Piirrä":
        i = 0
        while i < 3:
            i += 1
            print("#####")
    elif command == "lopeta":
        print("lopetetaan ohjelma. heippa!")
        break #break = lopetus käsky looppeihin
    elif command == "pelaa noppaa":

        noppa1 = noppa2 = heitot = 0
        while (noppa1 != 6 or noppa2 != 6):
            noppa1 = random.randint(1, 6)
            noppa2 = random.randint(1, 6)
            heitot = heitot + 1
        print(f"Tarvittiin {heitot:d} heittoa.")
        # heitetään kunnes molemmat nopat luku 6
    else:
        print("virheellinen komento. yritä uudelleen")

print("ohjelma sammutettu")

#noppa esim. 2 materiaalista

import random
toistot = 0
heitot_yhteensä = 0
while toistot < 100000:

    noppa1 = noppa2 = heitot = 0
    while (noppa1!=6 or noppa2!=6):
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        heitot = heitot + 1
    #print(f"Tarvittiin {heitot:d} heittoa.")
    toistot = toistot + 1
    heitot_yhteensä = heitot_yhteensä + heitot

heitot_keskimäärin = heitot_yhteensä/toistot
print(f"Heitot keskimäärin: {heitot_keskimäärin:6.2f}")