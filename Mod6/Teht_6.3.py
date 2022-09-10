
# funktio muunnokseen
def gallonToLitre(userInput):
    gallons = userInput
    litres = gallons * 3.785
    return litres

# pääohjelma

print("muutetaan gallonat litroiksi,kunnes negatiivinen tulos syötetään")
userInput = int(input("syötä gallonat:  "))
while userInput >= 0:

        litres = (gallonToLitre(userInput))
        print(f"Gallonat litroina: {litres:.2f},litraa")
        userInput = int(input("syötä gallonat:  "))

# ja viimeiseksi tulostus

print("negatiivinen tulos, ohjelma lopetettu")