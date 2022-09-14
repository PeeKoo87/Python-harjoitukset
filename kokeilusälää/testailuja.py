

userInput = int(input("anna kuukauden numero"))

kuukaudet = ("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu",
                 "Kesäkuu", "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")
kuukausi = kuukaudet[userInput-1]
#a_slice = kuukaudet[:]

#kuukausi = kevät
if kuukausi[3:5]:
    print("vuodenaika on kevät")
elif kuukausi[6:8]:
    print("vuodenaika on kesä")