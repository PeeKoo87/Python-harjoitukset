import math

luoti = float(input("Anna luotien määrä:"))
naula = float(input("Anna naulojen määrä:"))
leiviskä = float(input("Anna leiviskän määrä:"))


luoti_1 = (13.3)
naula_1 = (luoti_1 * 32)
leiviskä_1 = (naula_1 * 20)


le = (leiviskä * leiviskä_1)
lu = (luoti * luoti_1)
na = (naula * naula_1)

summa = (lu + le + na) / 1000




i, d = divmod(summa, 1)

print(f"Paino kiloina nykymittojen mukaan:",int(i), "ja", str(f"{d * 1000:.0f}"),"grammaa")