
print("syötä käyttäjätunnus ja salasana\n5 virheellistä lukitsee tunnukset")
count1 = 0
count2 = 0
user = ""
user = input("syötä tunnus:")

while user != "python":
    user = user.lower()
    count1 += 1

    if count1 == 5:
        print("pääsy evätty")
        break

    print("tunnus väärin,",(count1),"yritys")
    user = input("syötä tunnus")

if user == "python":
        print("tunnus oikein")

        passw = ""
        passw = input("syötä salasana:")
        while passw != "rules":
            count2 += 1
            print("salasana väärin,",(count2),"yritys")
            passw = passw.lower()

            if count2 ==5:
                print("pääsy evätty")
                break
            passw = input("syötä salasana")

        if passw == "rules":
                print("salasana oikein,tervetuloa")