# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

IntChk = int(input("anna kokonaisluku: "))
for i in range(2, IntChk):
    if IntChk % i == 0:
        print("luku ei ole alkuluku")
        break

else:
    print("luku on alkuluku")