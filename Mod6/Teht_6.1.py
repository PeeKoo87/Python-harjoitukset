import random

def rollDice():
    num = random.randint(1, 6)
    return num

while True:
    dieNum = rollDice()
    print(dieNum)
    if dieNum == 6:
        break