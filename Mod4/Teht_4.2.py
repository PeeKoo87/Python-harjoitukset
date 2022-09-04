#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
#niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
#Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,51cm

print("muunnetaan tuumat senteiksi, negatiivinen luku lopettaa ohjelman")
inch = float(input("syötä tuumat:"))


while inch >= 0:
    cm = inch * 2.51
    print(f"{inch} tuumaa on {cm:.2f} senttiä")
    inch = float(input("syötä tuumat: "))

print("ohjelma päättynyt")