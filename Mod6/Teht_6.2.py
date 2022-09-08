import random

#palauttaa nopan arvotun silmäluvun.
#tahkojen lukumäärä annetaan parametrinä.
def rollDice(sidesNum):
    num = random.randint(1, sidesNum)
    return num

sidesNum = int(input("Kuinka monta tahkoa? "))
while True:
    dieNum = rollDice(sidesNum)
    print(dieNum)
    if dieNum == sidesNum:
        break