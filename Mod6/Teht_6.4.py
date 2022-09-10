# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen palauttaman summan.


def calculate_sum(list):
    total = 0
    for i in list:
        total += i
        return total

a = [1, 2, 3, 4, 5]
b = [10, 15, 20]

print(sum(a))
print(calculate_sum(a))
print(calculate_sum(b))