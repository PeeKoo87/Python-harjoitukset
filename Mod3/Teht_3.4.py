#oma tehtävä, ei tarkista 400:lla jaollisuutta.

vuosiluku = float(input("Anna vuosiluku"))

vuosi1 = (vuosiluku/4)
if vuosi1.is_integer():
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")

#opettajan esimerkki!
v = int(input("anna vuosiluku: "))
if v % 4 == 0 and (v % 100 != 0 or v % 400 == 0):
    print("karkausvuosi")

else:("ei ole karkausvuosi")