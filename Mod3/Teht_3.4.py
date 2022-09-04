
vuosiluku = float(input("Anna vuosiluku"))

vuosi1 = (vuosiluku/4)
if vuosi1.is_integer():
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")