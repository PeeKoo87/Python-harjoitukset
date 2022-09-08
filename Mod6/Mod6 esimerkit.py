def laskeKolmionAla(kanta, korkeus):
    A = (kanta * korkeus) / 2
    return A

ka = float(input("anna kolmion kanta:   "))
ko = float(input("anna kolmion korkeus:  "))
pintaAla = laskeKolmionAla(ka, ko)
print(f"kolmion ala on {pintaAla:.2f}")
