import random
print("arvaa numero 1-10 väliltä")
x = random.randint(1, 10)
y = int(input("mikä on veikkauksesi?"))
while x != y:
    if x >= y:
        print("numero liian pieni!")
    if x <= y:
        print("numero liian suuri!")
    if x == y:
        print("oikein!")
    y = int(input("arvaa uudelleen!:  "))


print("voitit pelin!")