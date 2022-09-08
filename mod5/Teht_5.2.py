# 1.Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.

# 3.Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.

# 2.Vihje: listan alkioiden lajittelujärjestyksen voi kääntää
# antamalla sort-metodille argumentiksi reverse=True.

numbers = []
readingNumbers = True
while readingNumbers:
    strInput = input("anna luku: ")
    if strInput == "":
        readingNumbers = False
    else:
        numbers.append(int(strInput))


print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(numbers[0:5])
for number in numbers[:5]:
    print(number)