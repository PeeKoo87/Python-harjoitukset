
rahaa_taskussa = int(input("paljonko sinulla on rahaa?"))
maistuuko_kahvi = input("Maistuuko latte?")
laten_hinta = 5
kahvin_hinta = 3
teen_hinta = 2

if rahaa_taskussa >= laten_hinta and maistuuko_kahvi == "joo":
    print("osta latte")
    print("juo latte")
    rahaa_taskussa = rahaa_taskussa - laten_hinta

elif (rahaa_taskussa >= kahvin_hinta) and (maistuuko_kahvi == "joo"):
    print("osta normaali kahvi")
    rahaa_taskussa = rahaa_taskussa - kahvin_hinta

elif rahaa_taskussa >= teen_hinta:
    print("otan teen")
    rahaa_taskussa = rahaa_taskussa - teen_hinta
else:
    print("lähden kotiin")

if rahaa_taskussa == 0:
    print("rahat loppu")

else:
    print(f"sinulla on vielä {rahaa_taskussa} euroa taskussa.")

print("ohjelman suoritus loppui")



#ikä esimerkin juttuja
ikä = int(input("Anna ikä: "))
if 15<=ikä<18:
    paino = float(input("Anna paino (kg): "))
if ikä>=18 or (ikä>=15 and paino>=55):
    print("Lääkkeen käyttö on sallittua.")
else:
    print("lääkettä ei saa käyttää")