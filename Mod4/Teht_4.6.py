import random


circle = 0
i = 0
n = int(input("anna arvottujen pisteiden määrä: "))

while i <= n:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <=1:
        circle += 1
    i += 1

pi = 4 * circle / n

print(f"piin likiarvo on:{pi}")