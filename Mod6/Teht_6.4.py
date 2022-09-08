# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen palauttaman summan.


num_list = []

numQ = int(input("anna kokonaisluku: "))
while numQ != "":
    numQ = int(input("anna kokonaisluku: "))
    numQ.insert(1, num_list)
    numQ.append(num_list)


print(num_list)