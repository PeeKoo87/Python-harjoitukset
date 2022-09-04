# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

userInput = input("sano luku: ")
maxValue = minValue = int(userInput)

while userInput != "":
    userInput = input("sano luku: ")
    if userInput == "":
        break
    userInputInt = int(userInput)
    if userInputInt < minValue:
        minValue = int(userInput)
    if userInputInt > maxValue:
        maxValue = userInputInt

print(f"pienin arvo: {minValue}, suurin arvo: {maxValue}")