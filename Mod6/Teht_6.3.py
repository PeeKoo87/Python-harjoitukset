# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.

def gallonToLitre(userInput):
    gallons = userInput
    litres = gallons * 3.785
    return litres

print("muutetaan gallonat litroiksi")
userInput = int(input("syötä gallonat:  "))
while userInput >= 0:

        litres = (gallonToLitre(userInput))
        print(f"Gallonat litroina: {litres:.2f},litraa")
        userInput = int(input("syötä gallonat:  "))

print("negatiivinen tulos, ohjelma lopetettu")